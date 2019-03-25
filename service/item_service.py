from items.cpu import Cpu
from abc import ABCMeta, abstractclassmethod
class CpuService(metaclass = ABCMeta):
    """
        cpu直接服务类,修改和提供有关cpu状态信息
    """

    def __init__(self):
        # cpu词典, 将其name作为key, 本身作为value
        self._cpus = dict()

    @abstractclassmethod
    def prepareCpu( self , *names):
        """
            当程序初始化的时候, 创建所有的cpu item对象, 并初始化id和cpu name
        """
    

    @abstractclassmethod
    def updateCpu( self , cpusInfo ):
        """
            更新cpu最新状态信息
        """
        pass

    @abstractclassmethod
    def cpus(self):
        pass
