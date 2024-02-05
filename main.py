from DesktopCleaner import DesktopCleaner

if __name__ == "__main__":
    dC = DesktopCleaner()
    dC.path = "F:/Desktop/rozne/"
    dC.remove("tikto")
    if input("a:") == "a": 
        dC.go_back()