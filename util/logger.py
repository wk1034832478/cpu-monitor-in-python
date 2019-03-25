import time 
class Logger:
    """
        日志打印对象
    """
    __name = ''

    @staticmethod
    def get(className):
        logger = Logger()
        logger.__name = className
        return logger

    # @staticmethod
    def log(self, info):
        print( Logger.getTime(), self.__name, ' : ', info )
    
    @staticmethod
    def static_log(name, info):
        print(Logger.getTime() , self.__name, ' : ', info )
    
    @staticmethod
    def getTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 