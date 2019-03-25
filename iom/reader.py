from abc import  ABCMeta, abstractclassmethod
class Read(metaclass = ABCMeta):
    """
        读取固定文件,返回文件类的信息, 这是定义抽象层
    """
    @abstractclassmethod
    def read(self, filepath):
        """
            读取文件信息并返回内容
        """
