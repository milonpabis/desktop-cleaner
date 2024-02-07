import os
import winshell

class DesktopCleaner:


    def __init__(self):
        self.__path = None  # in terms of using remove_all() method
        self.__last_operation = None
        self.__last_deleted = []
        self.__created_directories = []
        self.__moved_files = []
        self.__empty_recycle_bin()


    def clean(self):
        self.__last_deleted = []
        files = os.listdir(self.__path)

        for file in files:
            try:
                if not os.path.isdir(self.__path + file):   # getting the extension of files and sorting them in directories of ext name
                    dotIndex = str(file).index(".")
                    extension = file[dotIndex+1:].upper()

                    if not os.path.exists(self.__path + extension):
                        os.makedirs(self.__path + extension)
                        self.__created_directories.append(self.__path + extension)

                    os.rename(self.__path + file, self.__path + extension + "/" + file) # moving files to their directories
                    self.__moved_files.append(self.__path + extension + "/" + file)

            except Exception:
                print(" E R R O R ! ")

        self.__last_operation = "clean"


    def remove(self, ext):
        self.__empty_recycle_bin()
        self.__last_deleted = []
        files = os.listdir(self.__path)

        for file in files:
            try:
                if not os.path.isdir(self.__path + file):   # getting the extension of files and 
                    dotIndex = str(file).index(".")             # moving them to the recycle bin if extension matches
                    extension = file[dotIndex+1:]

                    if extension == ext:
                        winshell.delete_file(self.__path + file, no_confirm=True)
                        self.__last_deleted.append(self.__path + file)

            except Exception:
                print("It's a directory!")

        self.__last_operation = "remove"


    def remove_all(self):    # removing all files from the directory, but not going into its subdirectories
        self.__empty_recycle_bin()
        self.__last_deleted = []
        
        files = os.listdir(self.__path)     # moving all files to the recycle bin
        for file in files:
            winshell.delete_file(self.__path + file, no_confirm=True)
            self.__last_deleted.append(self.__path + file)

        self.__last_operation = "remove"


    def go_back(self):
        if self.__last_operation == "remove":       # restoring files from the recycle bin
            items = list(winshell.recycle_bin())
            for item in items:
                winshell.undelete(item.original_filename())

        elif self.__last_operation == "clean":      # restoring files to their original state
            print(self.__moved_files)
            print(self.__created_directories)
            for file in self.__moved_files:
                temp = file.split("/")
                part = temp[:-2] + [temp[-1]]
                path = "/".join(part)
                print(path)
                os.rename(file, path)
            for directory in self.__created_directories:
                if not len(os.listdir(directory)):
                    os.rmdir(directory)
        self.__created_directories = []
        self.__moved_files = []
        

    def remove_recursive(self, ext):        # removing files from the directory and its subdirectories
        self.__empty_recycle_bin()
        queue = [self.__path]

        while queue:
            current = queue.pop(0)

            for file in os.listdir(current):
                if os.path.isdir(current + file):
                    queue.append(current + file + "/")

                else:
                    if file.endswith(ext):
                        winshell.delete_file(current + file, no_confirm=True)
                        self.__last_deleted.append(current + file)

        self.__last_operation = "remove"


    @property
    def path(self):
        return self.__path


    @path.setter
    def path(self, path):
        if os.path.exists(path):
            if path[-1] not in ("/", "\\"):
                path += "/"
            self.__path = path
        else:
            raise Exception("Path does not exist")
        

    def __empty_recycle_bin(self):
        try:
            winshell.recycle_bin().empty(confirm=False)
        except Exception:
            print("Recycle bin is already empty")
    

    

        