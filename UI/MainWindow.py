# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1150, 700)
        MainWindow.setMinimumSize(QSize(1150, 700))
        MainWindow.setMaximumSize(QSize(1150, 700))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-image: url(\"C:/Users/Milon/Downloads/galaxy_bg.jpg\");\n"
"}")
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionDirectory = QAction(MainWindow)
        self.actionDirectory.setObjectName(u"actionDirectory")
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font = QFont()
        font.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"	color: white;\n"
"	background-color: rgba(182, 57, 255, 80);\n"
"	\n"
"}")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.treeView = QTreeView(self.groupBox_4)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_6.addWidget(self.treeView)


        self.horizontalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"	color: white;\n"
"	background-color: rgba(182, 57, 255, 80);\n"
"	\n"
"}")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.treeView_2 = QTreeView(self.groupBox_5)
        self.treeView_2.setObjectName(u"treeView_2")
        self.treeView_2.setStyleSheet(u"background-color: rgba(192, 198, 223, 90);")

        self.horizontalLayout_7.addWidget(self.treeView_2)


        self.horizontalLayout.addWidget(self.groupBox_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(350, 0))
        self.groupBox_2.setMaximumSize(QSize(250, 16777215))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	color: white;\n"
"	background-color: rgba(182, 57, 255, 80);\n"
"	\n"
"}")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.leExtensions = QLineEdit(self.frame_6)
        self.leExtensions.setObjectName(u"leExtensions")
        self.leExtensions.setMinimumSize(QSize(0, 35))
        self.leExtensions.setStyleSheet(u"background-color: rgba(234, 220, 255, 190);\n"
"border-radius: 5px;\n"
"border: 1px solid rgba(182, 57, 255, 80);")

        self.verticalLayout_3.addWidget(self.leExtensions)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btRemove = QPushButton(self.frame_5)
        self.btRemove.setObjectName(u"btRemove")
        self.btRemove.setMinimumSize(QSize(0, 30))
        self.btRemove.setMaximumSize(QSize(16777215, 30))
        self.btRemove.setFont(font)
        self.btRemove.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(234, 220, 255, 190);\n"
"border-radius: 5px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(220, 220, 255, 190);\n"
"border-radius: 6px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btRemove)

        self.btRemoveAll = QPushButton(self.frame_5)
        self.btRemoveAll.setObjectName(u"btRemoveAll")
        self.btRemoveAll.setMinimumSize(QSize(80, 30))
        self.btRemoveAll.setMaximumSize(QSize(80, 30))
        self.btRemoveAll.setFont(font)
        self.btRemoveAll.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(234, 220, 255, 190);\n"
"border-radius: 5px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(220, 220, 255, 190);\n"
"border-radius: 6px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btRemoveAll)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"	color: white;\n"
"	background-color: rgba(182, 57, 255, 80);\n"
"	\n"
"}")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btOrganize = QPushButton(self.groupBox_3)
        self.btOrganize.setObjectName(u"btOrganize")
        self.btOrganize.setMinimumSize(QSize(100, 30))
        self.btOrganize.setMaximumSize(QSize(100, 30))
        self.btOrganize.setFont(font)
        self.btOrganize.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(234, 220, 255, 190);\n"
"border-radius: 5px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(220, 220, 255, 190);\n"
"border-radius: 6px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btOrganize)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(350, 0))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	color: white;\n"
"	background-color: rgba(182, 57, 255, 80);\n"
"	\n"
"}")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btUndo = QPushButton(self.groupBox)
        self.btUndo.setObjectName(u"btUndo")
        self.btUndo.setMinimumSize(QSize(100, 30))
        self.btUndo.setMaximumSize(QSize(100, 30))
        self.btUndo.setFont(font)
        self.btUndo.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(234, 220, 255, 190);\n"
"border-radius: 5px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(220, 220, 255, 190);\n"
"border-radius: 6px;\n"
"border: 1px solid rgba(182, 57, 255, 80);\n"
"}")

        self.horizontalLayout_5.addWidget(self.btUndo)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionDirectory.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.treeView.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: rgba(192, 198, 223, 90);", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Remove files", None))
        self.leExtensions.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex. jpg,png,zip", None))
        self.btRemove.setText(QCoreApplication.translate("MainWindow", u"Remove extensions", None))
        self.btRemoveAll.setText(QCoreApplication.translate("MainWindow", u"Remove all", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Organize folders", None))
        self.btOrganize.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Undo operations", None))
        self.btUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
    # retranslateUi

