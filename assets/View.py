from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
class View(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

