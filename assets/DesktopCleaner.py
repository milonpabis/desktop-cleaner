import os
import winshell
import datetime as dt

class DesktopCleaner:


    def __init__(self):
        self.__path = None  # in terms of using remove_all() method
        self.__logManager = LogStack()
        self.__last_operation = None
        self.__last_deleted = []
        self.__empty_recycle_bin()
        self.__last_log = None


    def clean(self):
        self.__last_deleted = []
        cd = []
        mf = []
        files = os.listdir(self.__path)

        for file in files:
            try:
                if not os.path.isdir(self.__path + file):   # getting the extension of files and sorting them in directories of ext name
                    dotIndex = str(file).index(".")
                    extension = file[dotIndex+1:].upper()

                    if not os.path.exists(self.__path + extension):
                        os.makedirs(self.__path + extension)
                        cd.append(self.__path + extension)

                    os.rename(self.__path + file, self.__path + extension + "/" + file) # moving files to their directories
                    mf.append(self.__path + extension + "/" + file)

            except Exception:
                print(" E R R O R ! ")

        self.__last_operation = "clean"
        self.__last_log = LogEntry(mf, cd)
        print(self.__last_log)
        self.__logManager.push_log(self.__last_log)


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
        self.__last_log = RLogEntry(self.__last_deleted)
        self.__logManager.push_log(self.__last_log)


    def remove_all(self):    # removing all files from the directory, but not going into its subdirectories
        self.__empty_recycle_bin()
        self.__last_deleted = []
        
        files = os.listdir(self.__path)     # moving all files to the recycle bin
        for file in files:
            winshell.delete_file(self.__path + file, no_confirm=True)
            self.__last_deleted.append(self.__path + file)

        self.__last_operation = "remove"
        self.__last_log = RLogEntry(self.__last_deleted)
        self.__logManager.push_log(self.__last_log)


    def go_back(self):
        print("TEST: ", self.__logManager.pop_log())
        print("!TEST")
        if self.__last_log is None:
            return
        
        if self.__last_operation == "remove":       # restoring files from the recycle bin
            items = list(winshell.recycle_bin())
            for item in items:
                winshell.undelete(item.original_filename())
                print(item.original_filename())

        elif self.__last_operation == "clean":      # restoring files to their original state
            for i in range(len(self.__last_log.files)):
                os.rename(self.__last_log.files[i], self.__last_log.old_names[i])
            for directory in self.__last_log.paths:
                if not len(os.listdir(directory)):
                    os.rmdir(directory)
        self.__last_log = None
        


    def remove_recursive(self, ext):        # removing files from the directory and its subdirectories
        self.__empty_recycle_bin()
        queue = [self.__path]

        while queue:
            current = queue.pop(0)

            for file in os.listdir(current):
                if os.path.isdir(current + file):
                    queue.append(current + file + "/")

                else:
                    if file.endswith(tuple(ext)):
                        winshell.delete_file(current + file, no_confirm=True)
                        self.__last_deleted.append(current + file)

        self.__last_operation = "remove"
        self.__last_log = RLogEntry(self.__last_deleted)
        self.__logManager.push_log(self.__last_log)


    @property
    def path(self):
        return self.__path


    @path.setter
    def path(self, path: str):
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



class LogEntry:

    def __init__(self, files: list[str], paths: list[str]):
        self.__files = files
        self.__paths = paths
        self.__old_names = []
        self.__translate()


    def __translate(self):
        for file in self.__files:
            temp = file.split("/")
            self.__old_names.append("/".join(temp[:-2] + [temp[-1]]))


    def __str__(self):
        res = [f"CREATED: {path}" for path in self.__paths]
        res += [f"{self.__old_names[i]} -> {self.__files[i]}" for i in range(len(self.__files))]
        return "\n".join(res)
        

    @property
    def files(self):
        return self.__files
    

    @property
    def paths(self):
        return self.__paths
    

    @property
    def old_names(self):
        return self.__old_names
    


class RLogEntry:

    def __init__(self, files: list[str]):
        self.__files = files


    def __str__(self):
        return "\n".join([f"REMOVED: {file}" for file in self.__files])


    @property
    def files(self):
        return self.__files



class LogStack:

    def __init__(self, log_path: str = "."):
        self.__logs : list[LogEntry, RLogEntry] = []
        self.__log_path = log_path
    

    def push_log(self, log: LogEntry or RLogEntry):
        try:
            with open(f"{self.__log_path}/log_{dt.datetime.now().strftime('%Y-%m-%d')}.txt", "a") as file:
                file.write(f"{dt.datetime.now().strftime('%H:%M:%S')}:\n{'-'*10}\n{log}\n{'-'*10}\n\n")
        except Exception:
            print("Error while saving the log")
        self.__logs.append(log)


    def pop_log(self) -> LogEntry or RLogEntry or None:
        if self.__is_empty():
            return None
        return self.__logs.pop(-1)


    def __is_empty(self) -> bool:
        return not bool(self.__logs)

    

    
    

    

        