import os


class DesktopCleaner:

    def __init__(self):
        self.__path = "."

    def clean(self):
        files = os.listdir(self.__path)
        for file in files:
            try:
                dotIndex = str(file).index(".")
                extension = file[dotIndex+1:].upper()
                if not os.path.exists(self.__path + extension):
                    os.makedirs(self.__path + extension)
                os.rename(self.__path + file, self.__path + extension + "/" + file)
            except Exception:
                print("It's a directory!")

    def remove(self, ext):
        files = os.listdir(self.__path)
        for file in files:
            try:
                dotIndex = str(file).index(".")
                extension = file[dotIndex+1:]
                if extension == ext:
                    os.remove(self.__path + file)
            except Exception:
                print("It's a directory!")

    def remove_all(self):
        if input("Are you sure? (Y/n): ") != "Y":
            return
        files = os.listdir(self.__path)
        for file in files:
            os.remove(self.__path + file)

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
        
    

    

        