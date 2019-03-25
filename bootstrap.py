from items.cpu import Cpu
from iom.io_factory import IOFactory
from util.logger import Logger
from util.stat_parser import StatParser
from util.util_factory import UtilFactory
from service.service_factory import ServiceFactory
from task.schedule_cpu_usage import ScheduleCpuUsageTask
from task.info_transfer import InfoTransfer
import queue
import time
import threading
from service.service_factory import ServiceFactory
class Bootstrap:
    """
        程序启动类,用以初始化程序工作,检查当前系统有多少个cpu,创建cpu词典, 
    """

    def __init__(self):
        self.__logger = Logger.get( Bootstrap.__name__ )
        self.__logger.log('系统正在启动...')
        # cpu使用率定时任务队列
        self.schedule_task_queue = queue.Queue()
        self.init_cpus()
        self.init_task()
        

    def init_cpus(self):
        """
            初始化cpu信息
        """
        fr = IOFactory.filereader()
        info = fr.read('/proc/stat')
        sp = UtilFactory.getStatParser()
        names = sp.getCpuNames( info )
        itemService = ServiceFactory.getItemService()
        itemService.prepareCpu( names )
    
    def init_task(self):
        t1 = ScheduleCpuUsageTask( self.schedule_task_queue )
        t1.start()
        # 定时更新cpu状态信息
        # 开启信息传输服务
        t2 = InfoTransfer(  self.schedule_task_queue  )
        t2.start()

    def update_cpu_info(self):
            """
                从线程消息队列当中取出最新cpu信息, 并更新到当前的cpu item当中
            """
            try:
                cpus_info = self.schedule_task_queue.get(block=False)
                self.__logger.log( cpus_info )
                # cis = ServiceFactory.getItemService()
                # cis.updateCpu( cpus_info )
            except queue.Empty:
                self.__logger.log( '暂时没有最新cpu信息' )
