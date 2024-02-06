from assets.DesktopCleaner import DesktopCleaner
from assets.View import View, QApplication

UITEST = True

if __name__ == "__main__":
    if not UITEST:
        dC = DesktopCleaner()
        dC.path = "F:/Desktop/rozne/"
        dC.remove("kitaka")
        if input("a:") == "a": 
            dC.go_back()
    else:
        app = QApplication()
        window = View()
        window.show()
        app.exec()