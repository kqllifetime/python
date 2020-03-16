#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#数据类型
#1.整数     -精确运算
print("整数：")
print(1,-1,0)   #十进制
print(0xff,0x00)    #十六进制 0x开头
print("\n")
#2.浮点数   -四舍五入存储
print("浮点数：")
print(1.23e10)  #科学计数法：1.11 -> 0.111e1
print(1.11e-3)
print("\n")
#3.字符串   -’.‘或者“.”或者’‘’.'''
print("字符串：")
print('I\'m OK!')   #  转义 \'
print('I\'m \"OK\"!')   #  转义 \"
print("I'm 'ok' \\")    #  转义 \\
print('\\\t\\')
print(r'\\\t\\')    #r'' 引号内的内容不转义
print('''hello      
world!''')      #多行打印
print(r'''hello \n
world''')       #r'''多行打印
print("\n")
#4.布尔值   -True 和 False
print("布尔值：")
print(True)
print(False)
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print("\n")
#5.空值     -None
print("空值:")
print(None)
print(type(None))
print("\n")


#变量
print("变量：")
x='abc'
y='bcd'
z=x
print(z)
x=y
print(x)
y=z
print(y)
print("\n")

#常量
print("常量：")
PI=3.1415926
print(PI)
print("\n")
#除法，整除，取余
print("除法，整除，取余：")
print(10/3)
print(10//3)
print(10%3)