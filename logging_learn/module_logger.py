#coding:utf8

'''
Created on 2016-4-12
针对不同用途的模块有不同的日志
实现：创建多个logger
'''
import sys
import logging

root_logger = logging.getLogger()

console_handler = logging.StreamHandler(sys.__stdout__)
console_handler.level = logging.DEBUG
console_logger = logging.getLogger('test')
console_logger.addHandler(console_handler)

file_handler = logging.FileHandler('test.log')
file_handler.level = logging.WARNING
file_logger = logging.getLogger('test.file')
file_logger.addHandler(file_handler)

console_logger.error('test')
file_logger.error('test')

print console_logger.parent is root_logger
print file_logger.parent is console_logger
print console_logger.getChild('file') is file_logger
