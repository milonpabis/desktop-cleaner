import os
import shutil
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
                        os.remove(self.__path + file)
                        self.__last_deleted.append(self.__path + file)
            except Exception:
                print("It's a directory!")

    def remove_all(self):
        self.__last_deleted = []
        if input("Are you sure? (Y/n): ") != "Y":
            return
        files = os.listdir(self.__path)
        for file in files:
            if os.path.isdir(self.__path + file):
                shutil.rmtree(self.__path + file)
            else:
                os.remove(self.__path + file)
            self.__last_deleted.append(self.__path + file)

    def go_back(self):
        items = list(winshell.recycle_bin())
        print(items)
        for item in self.__last_deleted:
            winshell.undelete(item)

    # save files somewhere and delete permamently only when there was no "goback" function called between operations
            # therefore have to create some type of history of operations
                # and create a location to save temp files to
        


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        if os.path.exists(path):
            self.__path = path
        else:
            raise Exception("Path does not exist")
        

    # TOO SLOW AND TAKES A LOT OF SPACE 
    def __back_up(self):
        if not os.path.exists(self.__bu_path):
            os.makedirs(self.__bu_path)
        for file in os.listdir(self.__bu_path):
            if os.path.isdir(self.__bu_path + file):
                shutil.rmtree(self.__bu_path + file)
            else:
                os.remove(self.__bu_path + file)
        files = os.listdir(self.__path)
        for file in files:
            print(file)
            if os.path.isdir(self.__path + file):
                shutil.copytree(self.__path + file, self.__bu_path + file)
            else:
                shutil.copy(self.__path + file, self.__bu_path + file)
        
    

    

        