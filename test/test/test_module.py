#!/usr/bin/env python3.8        #指定解释器
# -*- coding: utf-8 -*-         #指定编码方式

'a test module'                 #首行的字符代表备注

__author__='kql'                #特殊变量，给予特殊意义

import sys                      #导入模块

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello World')
    elif len(args)==2:
        print('Hello,%s'%args[1])
    else:
        print('Too many arguments!')

def _private_1(name):               #私有函数，名称前加‘_'
    return 'Hello,%s'%name

def _private_2(name):
    return 'Hi,%s'%name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__=='__main__':            #判断是否为命令行调用
    test()

