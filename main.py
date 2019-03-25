#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from items.cpu import Cpu
from iom.reader import Read
from iom.implements.file_reader import FileReader
from util.implements.stat_parser_imply import StatParserImply 
from bootstrap import Bootstrap
# read = FileReader()
# s = StatParserImply()
# info = read.read('/proc/stat')
# print( info )
# s.parse( info )
b = Bootstrap()

