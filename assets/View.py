from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileSystemModel
from PySide6.QtCore import QDir
class View(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet('QMainWindow {background-image: url("UI/images/galaxy_bg.jpg");}')
        self.setup_tree(self.treeView)
        self.treeView.clicked.connect(self.show_selected)
        self.btUndo.clicked.connect(self.undo_pressed)
        self.btOrganize.clicked.connect(self.organize_pressed)
        self.btRemove.clicked.connect(self.remove_pressed)
        self.btRemoveAll.clicked.connect(self.remove_all_pressed)


    def setup_tree(self, view, path=""):
        model = QFileSystemModel()
        model.setRootPath(QDir.rootPath())
        view.setModel(model)
        if path:
            view.setRootIndex(model.index(path))
        view.setColumnWidth(0, 400)
        view.setSortingEnabled(True)
        view.setAnimated(True)
        view.setColumnHidden(1, True)
        view.setColumnHidden(3, True)


    def show_selected(self):
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        self.setup_tree(self.treeView_2, path)
        print(path)

    def undo_pressed(self):
        print("undo")

    def organize_pressed(self):
        print("organize")

    def remove_pressed(self):
        print("remove")

    def remove_all_pressed(self):
        print("remove all")
