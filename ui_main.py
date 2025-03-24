# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_cbs.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 860)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMinimumSize(QSize(425, 500))
        self.main_body.setStyleSheet(u"QWidget#main_body\n"
"{\n"
"background-color: rgb(92, 114, 133);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.main_body)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.contentWidget = QWidget(self.main_body)
        self.contentWidget.setObjectName(u"contentWidget")
        self.verticalLayout = QVBoxLayout(self.contentWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, -1)
        self.errorsLabel = QLabel(self.contentWidget)
        self.errorsLabel.setObjectName(u"errorsLabel")
        font = QFont()
        font.setPointSize(12)
        self.errorsLabel.setFont(font)

        self.verticalLayout.addWidget(self.errorsLabel)

        self.logTableWidget = QTableWidget(self.contentWidget)
        if (self.logTableWidget.columnCount() < 3):
            self.logTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.logTableWidget.rowCount() < 2):
            self.logTableWidget.setRowCount(2)
        self.logTableWidget.setObjectName(u"logTableWidget")

        self.verticalLayout.addWidget(self.logTableWidget)

        self.fixLabel = QLabel(self.contentWidget)
        self.fixLabel.setObjectName(u"fixLabel")
        self.fixLabel.setFont(font)

        self.verticalLayout.addWidget(self.fixLabel)

        self.fixText = QTextEdit(self.contentWidget)
        self.fixText.setObjectName(u"fixText")

        self.verticalLayout.addWidget(self.fixText)

        self.widget = QWidget(self.contentWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 24))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fixIssueButton = QPushButton(self.widget)
        self.fixIssueButton.setObjectName(u"fixIssueButton")
        self.fixIssueButton.setMinimumSize(QSize(124, 24))
        self.fixIssueButton.setMaximumSize(QSize(124, 24))
        font1 = QFont()
        font1.setPointSize(9)
        self.fixIssueButton.setFont(font1)

        self.horizontalLayout.addWidget(self.fixIssueButton)

        self.operationLine = QLineEdit(self.widget)
        self.operationLine.setObjectName(u"operationLine")
        self.operationLine.setReadOnly(True)

        self.horizontalLayout.addWidget(self.operationLine)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.contentWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.openDocumentationButton_2 = QPushButton(self.widget_2)
        self.openDocumentationButton_2.setObjectName(u"openDocumentationButton_2")
        self.openDocumentationButton_2.setMinimumSize(QSize(124, 24))
        self.openDocumentationButton_2.setMaximumSize(QSize(124, 24))
        self.openDocumentationButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.openDocumentationButton_2)

        self.showLoggingButton_2 = QPushButton(self.widget_2)
        self.showLoggingButton_2.setObjectName(u"showLoggingButton_2")
        self.showLoggingButton_2.setMinimumSize(QSize(124, 24))
        self.showLoggingButton_2.setMaximumSize(QSize(124, 24))
        self.showLoggingButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.showLoggingButton_2)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout_2.addWidget(self.contentWidget, 3, 0, 1, 1)

        self.headerWidget = QWidget(self.main_body)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setMaximumSize(QSize(16777215, 26))
        self.headerWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.gridLayout_4 = QGridLayout(self.headerWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.headerWidget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.main_body)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.loadLogButton = QPushButton(self.widget_3)
        self.loadLogButton.setObjectName(u"loadLogButton")
        self.loadLogButton.setMinimumSize(QSize(124, 24))
        self.loadLogButton.setMaximumSize(QSize(124, 24))

        self.horizontalLayout_3.addWidget(self.loadLogButton)

        self.pathLine = QLineEdit(self.widget_3)
        self.pathLine.setObjectName(u"pathLine")
        self.pathLine.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.pathLine)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.main_body, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.errorsLabel.setText(QCoreApplication.translate("MainWindow", u"Errors Found:", None))
        ___qtablewidgetitem = self.logTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtablewidgetitem1 = self.logTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Error Code", None));
        ___qtablewidgetitem2 = self.logTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        self.fixLabel.setText(QCoreApplication.translate("MainWindow", u"Suggestions:", None))
        self.fixIssueButton.setText(QCoreApplication.translate("MainWindow", u"Fix Selected", None))
        self.operationLine.setText("")
        self.operationLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No operation running...", None))
        self.openDocumentationButton_2.setText(QCoreApplication.translate("MainWindow", u"Open Documentation", None))
        self.showLoggingButton_2.setText(QCoreApplication.translate("MainWindow", u"Show Logging", None))
        self.loadLogButton.setText(QCoreApplication.translate("MainWindow", u"Open CBS File", None))
        self.pathLine.setText("")
        self.pathLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File path...", None))
    # retranslateUi

