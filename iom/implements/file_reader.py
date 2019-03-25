from iom.reader import Read
class FileReader( Read ):
    """
    """

    def __init__(self):
        pass

    def read(self, filepath):
        info = ''
        with open(filepath) as f:
            info = f.read()
        return info