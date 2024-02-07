from UI.MainWindow import Ui_MainWindow
from UI.RemoveConfirm import Ui_Dialog
from PySide6.QtWidgets import QMainWindow, QApplication, QFileSystemModel, QDialog
from PySide6.QtCore import QDir
from PySide6.QtGui import QIcon
import winreg
from assets.DesktopCleaner import DesktopCleaner



class View(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.dCleaner = DesktopCleaner()        # connecting the logic
        self.setupUi(self)
        self.setStyleSheet('QMainWindow {background-image: url("UI/images/galaxy_bg.jpg");}')
        self.setWindowTitle("Desktop Cleaner v1.0")
        self.setWindowIcon(QIcon("UI/images/ico.jpg"))
        self.setup_tree(self.treeView)
        self.treeView.clicked.connect(self.show_selected)
        self.btUndo.clicked.connect(self.undo_pressed)
        self.btOrganize.clicked.connect(self.organize_pressed)
        self.btRemove.clicked.connect(self.remove_pressed)
        self.btRemoveAll.clicked.connect(self.remove_all_pressed)
        self.expand_tree()                      # setting the desktop as the selected one
        


    def setup_tree(self, view, path=""):        # filling the tree with system files
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


    def show_selected(self):                    # showing the selected path in the second tree
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        self.dCleaner.path = path
        self.lPath.setText(path)
        self.setup_tree(self.treeView_2, path)

    def expand_tree(self):                      # setting the desktop as the selected one
        desktop_path = get_desktop_path()
        self.dCleaner.path = desktop_path       # setting the initial path for the logic
        desktop_index = self.treeView.model().index(desktop_path)
        if desktop_index.isValid():
            self.treeView.setCurrentIndex(desktop_index)
            self.show_selected()
            self.lPath.text = desktop_path

        
        

    def undo_pressed(self):
        self.dCleaner.go_back()

    def organize_pressed(self):
        self.dCleaner.clean()

    def remove_pressed(self):
        if not self.leExtensions.text():
            return
        extensions = self.leExtensions.text().split(",")
        self.dCleaner.remove_recursive(extensions)

    def remove_all_pressed(self):       
        dialog = AcceptDialog()
        dialog.exec()
        if dialog.returnValue:
            self.dCleaner.remove_all()
        




class AcceptDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet('QDialog {background-image: url("UI/images/dialog_bg.jpg");}')
        self.setWindowTitle("Confirm")
        self.setWindowIcon(QIcon("UI/images/ico.jpg"))
        self.returnValue = 0
        self.pushButton.clicked.connect(lambda: self.accept(1))
        self.pushButton_2.clicked.connect(lambda: self.accept(0))

    def accept(self, val):
        self.returnValue = val
        super().accept()


KEYPATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"

def get_desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEYPATH, 0, winreg.KEY_READ)
    try:
        value, _ = winreg.QueryValueEx(key, "Desktop")
        return value
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        winreg.CloseKey(key)
    return None
