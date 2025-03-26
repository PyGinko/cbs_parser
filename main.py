import re
import json
import subprocess
import sys
import ctypes

# Import UI
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QRunnable, QThreadPool, Signal, QObject
from ui_main import Ui_MainWindow


# Load error solutions from a JSON file
with open("../assets/errors_master.json", "r", encoding="utf-8") as f:
    ERROR_SOLUTIONS = json.load(f)

# Worker Classes
class FixWorkerSignals(QObject):
    finished = Signal()
    error = Signal(str)

class FixWorker(QRunnable):
    def __init__(self, command):
        super().__init__()
        self.command = command
        self.signals = FixWorkerSignals()

    def run(self):
        try:
            for cmd in self.command:
                subprocess.run(cmd, shell=True, check=True)
            self.signals.finished.emit()
        except subprocess.CalledProcessError as e:
            self.signals.error.emit(f"Error: {str(e)}")

# Main Class
class CBSLogAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()

        # Icon
        self.setWindowIcon(QIcon("../assets/logs.png"))

        # Name
        self.setWindowTitle("CBS Parser")

        # Initial State
        self.ui.logTableWidget.setRowCount(0)
        self.reset_text()

        # Connect buttons to functions
        self.ui.loadLogButton.clicked.connect(self.load_cbs_log)
        self.ui.fixIssueButton.clicked.connect(self.apply_fix)
        self.ui.logTableWidget.itemSelectionChanged.connect(self.changeText)

    def reset_text(self):
        self.ui.descriptionText.setText("Select an error...")
        self.ui.fixText.setText("Select an error...")

    def changeText(self):
        self.display_fix_details()
        self.display_desc_details()

    def load_cbs_log(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CBS.log File", "", "Log Files (*.log)")
        if file_path:
            self.parse_cbs_log(file_path)

    def parse_cbs_log(self, file_path):
        """Parses CBS.log and populates the table with timestamp, HRESULT, and error message."""

        error_pattern = re.compile(
            r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\s*Error\s*CBS\s*(.+?)\s*\[HRESULT = (0x[0-9A-Fa-f]+)'
        )

        self.ui.logTableWidget.setRowCount(0)  # Clear existing rows

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = error_pattern.search(line)
                if match:
                    timestamp = match.group(1)
                    message = match.group(2).strip()
                    error_code = match.group(3) if match.group(3) else "N/A"

                    row_position = self.ui.logTableWidget.rowCount()
                    self.ui.logTableWidget.insertRow(row_position)
                    self.ui.logTableWidget.setItem(row_position, 0, QTableWidgetItem(timestamp))
                    self.ui.logTableWidget.setItem(row_position, 1, QTableWidgetItem(error_code))
                    self.ui.logTableWidget.setItem(row_position, 2, QTableWidgetItem(message))

        self.ui.logTableWidget.resizeColumnsToContents()
        self.reset_text()
        self.ui.pathLine.setText(file_path)

    def display_fix_details(self):
        """Displays the solution when an error is selected."""
        selected_row = self.ui.logTableWidget.currentRow()
        if selected_row != -1:
            error_code = self.ui.logTableWidget.item(selected_row, 1).text()
            error_details = ERROR_SOLUTIONS.get(error_code, {})

            mitigation_text = error_details.get("mitigation", "No solution found")
            self.ui.fixText.setText(mitigation_text)

    def display_desc_details(self):
        selected_row = self.ui.logTableWidget.currentRow()
        if selected_row != -1:
            error_code = self.ui.logTableWidget.item(selected_row, 1).text()
            error_details = ERROR_SOLUTIONS.get(error_code, {})

            message_text = error_details.get("message", "")
            description_text = error_details.get("description", "")
            updated_text = "No Information found"
            if message_text or description_text:
                updated_text = f"{message_text}<br>{description_text}"
            self.ui.descriptionText.setText(updated_text)

    def apply_fix(self):
        """Runs the fix when clicking 'Fix Selected Issue'."""

        # Check if running as admin
        if not ctypes.windll.shell32.IsUserAnAdmin():
            QMessageBox.warning(self, "Administrator Required", "This action requires administrator privileges.")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            return  # Exit to avoid running without admin

        selected_row = self.ui.logTableWidget.currentRow()
        if selected_row != -1:
            error_code = self.ui.logTableWidget.item(selected_row, 1).text()
            fix_message = ERROR_SOLUTIONS.get(error_code)

            if fix_message:
                self.ui.fixIssueButton.setEnabled(False)  # Disable button during fix
                self.ui.operationLine.setText("Applying fix...")  # Show progress

                # Determine fix commands
                if "dism" in fix_message.lower():
                    command = [["dism", "/online", "/cleanup-image", "/restorehealth"]]
                elif "SoftwareDistribution" in fix_message:
                    command = [
                        ["net", "stop", "wuauserv"],
                        ["rmdir", "/s", "/q", "C:\\Windows\\SoftwareDistribution"],
                        ["net", "start", "wuauserv"]
                    ]
                else:
                    QMessageBox.warning(self, "No Fix Available", "No predefined fix for this error.")
                    return

                # Run fix in a separate thread
                worker = FixWorker(command)
                worker.signals.finished.connect(self.fix_completed)
                worker.signals.error.connect(self.fix_failed)
                self.threadpool.start(worker)

    def fix_completed(self):
        self.ui.fixIssueButton.setEnabled(True)
        self.ui.operationLine.setText("Fix applied successfully!")
        QMessageBox.information(self, "Success", "The fix has been applied successfully.")

    def fix_failed(self, error_message):
        self.ui.fixIssueButton.setEnabled(True)
        self.ui.operationLine.setText("Fix failed.")
        QMessageBox.critical(self, "Error", error_message)


app = QApplication([])
main_win = CBSLogAnalyzer()
main_win.show()
app.exec()