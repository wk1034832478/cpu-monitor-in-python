from util.stat_parser import StatParser
import re
from util.logger import Logger
from items.cpu import Cpu
class StatParserImply( StatParser ):
    """
        实现类
    """
    def __init__(self):
        self.logger = Logger.get( StatParserImply.__name__ )

    def parse(self, info) -> list:
        """
            返回一个元祖列表,每个元祖列表具有以下元素: name totaltime(所有时间) idletime(睡眠时间),可以根据两个这样的数据计算cpu使用率
        """
        l = list()
        userfulInfo = self.getUsefulInfo( info )
        self.logger.log( userfulInfo )
        for index in range(len(userfulInfo)):
            ui = userfulInfo[index]
            name = ''
            totaltime = 0
            idletime = 0
            datas = re.split(r'\s+', ui )
            for index in range(len(datas)):
                if  index == 0:
                    name = datas[index]
                    continue
                if  index == 4:
                    idletime = datas[index]
                totaltime += int( datas[index] )
            l.append( (name, totaltime, idletime) )
        return l

    def getUsefulInfo(self, info):
        """
            获取关于cpu使用情况的前几行信息
        """
        usefulInfo = re.findall(r'cpu.*', info);
        if usefulInfo:
            return  usefulInfo
        else:
            raise Exception('/proc/stat文件没有有用的信息,请检查系统资源是否完整,是否存在/proc/stat动态文件信息')
    
    def getCpuNames(self, info) -> list:
        self.logger.log( '正在检查系统cpu...' )
        userfulInfo = self.getUsefulInfo( info )
        l = list()
        for ui in userfulInfo:
            name = re.split(r'\s+', ui )[0]
            if not re.search(r'[0-9]', name):
                continue
            self.logger.log( 'cpu名称:' + name )
            l.append(  name )
        return l
        
        