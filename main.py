from assets.DesktopCleaner import DesktopCleaner
from assets.View import View, QApplication


if __name__ == "__main__":
    app = QApplication()
    window = View()
    window.show()
    app.exec()       

# TODO:
    # create class Logs with history of operations and its data
