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
        MainWindow.resize(598, 682)
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
        self.fileWidget = QWidget(self.main_body)
        self.fileWidget.setObjectName(u"fileWidget")
        self.fileWidget.setMinimumSize(QSize(0, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.fileWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.loadLogButton = QPushButton(self.fileWidget)
        self.loadLogButton.setObjectName(u"loadLogButton")
        self.loadLogButton.setMinimumSize(QSize(124, 24))
        self.loadLogButton.setMaximumSize(QSize(124, 24))

        self.horizontalLayout_3.addWidget(self.loadLogButton)

        self.pathLine = QLineEdit(self.fileWidget)
        self.pathLine.setObjectName(u"pathLine")
        self.pathLine.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.pathLine)


        self.gridLayout_2.addWidget(self.fileWidget, 0, 0, 1, 1)

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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTableWidget.sizePolicy().hasHeightForWidth())
        self.logTableWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.logTableWidget)

        self.descriptionLabel = QLabel(self.contentWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setFont(font)

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.descriptionText = QTextEdit(self.contentWidget)
        self.descriptionText.setObjectName(u"descriptionText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.descriptionText.sizePolicy().hasHeightForWidth())
        self.descriptionText.setSizePolicy(sizePolicy1)
        self.descriptionText.setMaximumSize(QSize(16777215, 99))

        self.verticalLayout.addWidget(self.descriptionText)

        self.fixLabel = QLabel(self.contentWidget)
        self.fixLabel.setObjectName(u"fixLabel")
        self.fixLabel.setFont(font)

        self.verticalLayout.addWidget(self.fixLabel)

        self.fixText = QTextEdit(self.contentWidget)
        self.fixText.setObjectName(u"fixText")
        sizePolicy1.setHeightForWidth(self.fixText.sizePolicy().hasHeightForWidth())
        self.fixText.setSizePolicy(sizePolicy1)
        self.fixText.setMaximumSize(QSize(16777215, 198))

        self.verticalLayout.addWidget(self.fixText)

        self.fixWidget = QWidget(self.contentWidget)
        self.fixWidget.setObjectName(u"fixWidget")
        self.fixWidget.setMinimumSize(QSize(0, 24))
        self.horizontalLayout = QHBoxLayout(self.fixWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fixIssueButton = QPushButton(self.fixWidget)
        self.fixIssueButton.setObjectName(u"fixIssueButton")
        self.fixIssueButton.setMinimumSize(QSize(124, 24))
        self.fixIssueButton.setMaximumSize(QSize(124, 24))
        font1 = QFont()
        font1.setPointSize(9)
        self.fixIssueButton.setFont(font1)

        self.horizontalLayout.addWidget(self.fixIssueButton)

        self.operationLine = QLineEdit(self.fixWidget)
        self.operationLine.setObjectName(u"operationLine")
        self.operationLine.setReadOnly(True)

        self.horizontalLayout.addWidget(self.operationLine)


        self.verticalLayout.addWidget(self.fixWidget)

        self.optionsWidget = QWidget(self.contentWidget)
        self.optionsWidget.setObjectName(u"optionsWidget")
        self.optionsWidget.setMinimumSize(QSize(0, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.optionsWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.openDocumentationButton = QPushButton(self.optionsWidget)
        self.openDocumentationButton.setObjectName(u"openDocumentationButton")
        self.openDocumentationButton.setMinimumSize(QSize(124, 24))
        self.openDocumentationButton.setMaximumSize(QSize(124, 24))
        self.openDocumentationButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.openDocumentationButton)

        self.showLoggingButton = QPushButton(self.optionsWidget)
        self.showLoggingButton.setObjectName(u"showLoggingButton")
        self.showLoggingButton.setMinimumSize(QSize(124, 24))
        self.showLoggingButton.setMaximumSize(QSize(124, 24))
        self.showLoggingButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.showLoggingButton)


        self.verticalLayout.addWidget(self.optionsWidget)


        self.gridLayout_2.addWidget(self.contentWidget, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.main_body, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loadLogButton.setText(QCoreApplication.translate("MainWindow", u"Open CBS File", None))
        self.pathLine.setText("")
        self.pathLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File path...", None))
        self.errorsLabel.setText(QCoreApplication.translate("MainWindow", u"Errors Found:", None))
        ___qtablewidgetitem = self.logTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtablewidgetitem1 = self.logTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Error Code", None));
        ___qtablewidgetitem2 = self.logTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Error Description:", None))
        self.fixLabel.setText(QCoreApplication.translate("MainWindow", u"Suggestions and Fixes:", None))
        self.fixIssueButton.setText(QCoreApplication.translate("MainWindow", u"Fix Selected", None))
        self.operationLine.setText("")
        self.operationLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No operation running...", None))
        self.openDocumentationButton.setText(QCoreApplication.translate("MainWindow", u"Open Documentation", None))
        self.showLoggingButton.setText(QCoreApplication.translate("MainWindow", u"Show Logging", None))
    # retranslateUi

