from util.implements.stat_parser_imply import StatParserImply
from util.stat_parser import StatParser
class UtilFactory():

    # 静态对象
    __spi = StatParserImply()

    @staticmethod
    def getStatParser() -> StatParser:
        return UtilFactory.__spi