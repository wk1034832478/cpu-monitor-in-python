from abc import ABCMeta, abstractclassmethod
from items.cpu import Cpu
class StatParser(metaclass= ABCMeta):
    """
        解析/proc/stat文件数据内容
    """

    @abstractclassmethod
    def parse(self, info) -> list:
        pass
    
    @abstractclassmethod
    def getCpuNames(self, info) -> list:
        """
            获取系统所有的cpu名称
        """
        pass