from iom.implements.file_reader import FileReader
class IOFactory:
    
    __filereader =  FileReader()

    def __init__(self):
        pass

    @staticmethod
    def filereader() -> FileReader:
        return IOFactory.__filereader
