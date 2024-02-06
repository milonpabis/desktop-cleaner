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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QListView, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 0))
        self.frame_4.setMaximumSize(QSize(400, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.frame_4)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_2.addWidget(self.treeWidget)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setMaximumSize(QSize(400, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget = QListView(self.frame_5)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_3.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuVersion = QMenu(self.menubar)
        self.menuVersion.setObjectName(u"menuVersion")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuVersion.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionInfo)
        self.menuMenu.addAction(self.actionUndo)
        self.menuMenu.addAction(self.actionDirectory)
        self.menuVersion.addAction(self.actionVersion)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionDirectory.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"folder1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"a", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"c", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"c", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"folder2", None));
        ___qtreewidgetitem6 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"gg", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"ggg", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"ggg", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"plik.txt", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"folder3", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuVersion.setTitle(QCoreApplication.translate("MainWindow", u"Version", None))
    # retranslateUi

