# -*- coding: utf-8 -*-
from service.service_factory import ServiceFactory
import socket
from threading import Thread
from util.logger import Logger
class InfoTransfer( Thread ):
    """
        提供套接字传输功能,可以直接直接通过端口信息传输,获取当前cpu使用状态
    """
    def __init__(self, schedule_task_queue):
        Thread.__init__(self)
        self.__logger = Logger.get( InfoTransfer.__name__ )
        self.schedule_task_queue = schedule_task_queue

    def run(self):
        
        s = socket.socket()
        hostname = socket.gethostname()
        port = 8081
        self.__logger.log('正在监听 %d 端口' %  ( port ) )
        s.bind( ('0.0.0.0', port) )
        s.listen( 0 )

        while True:
            c, addr = s.accept()
            cpus = ServiceFactory.getItemService().cpus()
            self.__logger.log( '收到新的客户端请求, 正在发送信息...'  )
            c.send( cpus.encode('utf-8') )
            
                