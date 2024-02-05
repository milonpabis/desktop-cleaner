import os
import winshell

BACK_UP_PATH = "F:/Desktop/BackUp/"

class DesktopCleaner:

    def __init__(self):
        self.__path = "."
        self.__bu_path = BACK_UP_PATH
        self.__last_deleted = []
        try:
            winshell.recycle_bin().empty(confirm=False)
        except:
            print("Recycle bin is empty")

    def clean(self):
        self.__last_deleted = []
        files = os.listdir(self.__path)
        for file in files:
            try:
                if not os.path.isdir(self.__path + file):
                    dotIndex = str(file).index(".")
                    extension = file[dotIndex+1:].upper()
                    if not os.path.exists(self.__path + extension):
                        os.makedirs(self.__path + extension)
                    os.rename(self.__path + file, self.__path + extension + "/" + file)
            except Exception:
                print(" E R R O R ! ")

    def remove(self, ext):
        self.__last_deleted = []
        files = os.listdir(self.__path)
        for file in files:
            try:
                if not os.path.isdir(self.__path + file):
                    dotIndex = str(file).index(".")
                    extension = file[dotIndex+1:]
                    if extension == ext:
                        winshell.delete_file(self.__path + file, no_confirm=True)
                        self.__last_deleted.append(self.__path + file)
            except Exception:
                print("It's a directory!")

    def remove_all(self):
        self.__last_deleted = []
        if input("Are you sure? (Y/n): ") != "Y":
            return
        files = os.listdir(self.__path)
        for file in files:
            winshell.delete_file(self.__path + file, no_confirm=True)
            self.__last_deleted.append(self.__path + file)

    def go_back(self):
        items = list(winshell.recycle_bin())
        for item in items:
            winshell.undelete(item.original_filename())

    # TODO:
            # - add a method to remove all files with a given extension recursively
            # - add a go_back option to restore files that had been put into directories
        


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        if os.path.exists(path):
            self.__path = path
        else:
            raise Exception("Path does not exist")
        
    

    

        