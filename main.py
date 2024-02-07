from assets.DesktopCleaner import DesktopCleaner
from assets.View import View, QApplication
import datetime as dt
TEST = False

if __name__ == "__main__":
    if not TEST:
        app = QApplication()
        window = View()
        window.show()
        app.exec()       
    else:
        print(dt.datetime.now().strftime('%Y-%m-%d'))

# TODO:
    # connect logManager to functions