from threading import Thread
from service.service_factory import ServiceFactory
from util.logger import Logger
from util.util_factory import UtilFactory
from iom.io_factory import IOFactory
import time
import queue
class ScheduleCpuUsageTask( Thread ):

    def __init__(self, infoQueue ):
        """
            线程进行初始化, 首先调用Thread的构造方法
        """
        Thread.__init__(self)
        self.__logger = Logger.get( ScheduleCpuUsageTask.__name__ )
        self.__logger.log( '正在启动cpu使用率计算线程' )
        self.__infoQueue = infoQueue
        self.filereader = IOFactory.filereader()
        self.sp = UtilFactory.getStatParser()
        self.lastCpuInfoList = None

    def run(self):
        while True:
            l = list()
            try:
                signal = self.__infoQueue.get(block=False)
            except queue.Empty:
                self.__logger.log( '队列中没有任何信息!' )
            
            info = self.filereader.read( '/proc/stat' )
            cpu_info_list = self.sp.parse( info )
            # 计算cpu使用率
            if self.lastCpuInfoList:
                for index in range( len(cpu_info_list) ):
                    cpu_info1 = cpu_info_list[index]
                    cpu_info2 = self.lastCpuInfoList[index]

                    dIdletime = int(cpu_info1[ 2 ]) - int(cpu_info2[ 2 ])
                    dTotaltime = int(cpu_info1[ 1 ]) - int(cpu_info2[ 1 ])
                    usage = 100 * ( dTotaltime - dIdletime ) / ( dTotaltime )
                    #usage = round(usage*100,2)
                    self.__logger.log( '当前cpu名称: %s 总时间: %s 总睡眠时间: %s' % cpu_info1 )
                    self.__logger.log( "cpu-%s 使用率: %.2f %s " % ( cpu_info1[0], usage, '%'  ) )
                    l.append( (cpu_info1[0], usage) )

            self.lastCpuInfoList = cpu_info_list
            # 更新数据
            cis = ServiceFactory.getItemService()
            cis.updateCpu( l )
            self.__infoQueue.put( l )
            # 进入睡眠, 注意睡眠的时间单位为s
            time.sleep( 0.5 )