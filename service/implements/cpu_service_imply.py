from items.cpu import Cpu
from service.item_service import CpuService
import re
from util.logger import Logger
class CpuServiceImply( CpuService ):

    def __init__(self):
        CpuService.__init__(self)
        self.__logger = Logger.get( CpuServiceImply.__name__ )

    def prepareCpu( self , names):
        self.__logger.log(  names )
        for name in names:
            self.__logger.log('正在创建cpu:' + name)
            self._cpus[ name ] = Cpu( self.getIdByName( name ), name )
    
    def getIdByName(self, name):
        return int( re.search(r'[0-9]{1,2}', name)[0] )

    
    def updateCpu( self , cpusInfo ):
        for cpuInfo in cpusInfo:
            self.__logger.log( '正在修改 %s 状态信息' % ( cpuInfo[0] ) )
            cpu = None
            try:
                cpu = self._cpus[ cpuInfo[0] ]
            except:
                # 总使用率
                cpu = Cpu( "10000" ,cpuInfo[0] )
            cpu.usage = float( cpuInfo[1] )
            self._cpus[ cpuInfo[0] ] = cpu
    
    def cpus(self):
        cpu_info = ''
        for cpu_name, cpu in self._cpus.items():
            name = cpu.name
            usage = cpu.usage
            if not usage:
                usage = 0.00
            print( '----', name , usage )
            cpu_info = cpu_info + ' || ' + name + ' - ' + str(usage)
        return cpu_info


