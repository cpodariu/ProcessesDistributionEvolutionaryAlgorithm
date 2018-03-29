class Controller:
    def __init__(self):
        self.__path_to_files = "C:/Users/cpodariu/Workspace/AI/Lab2/data/"
        self.__sudoku = None
        self.__files = ["example1.txt"]

    def read_string(self, example):
        file_path = self.__files[example]
        with open(self.__path_to_files + file_path) as f:
            array = [[int(x) for x in line.split()] for line in f]
        return array
