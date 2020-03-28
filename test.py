#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

'import module test'

#导入方式
#from test.test.test_module import test
from test.test import test_module
#模块的组织方式:Package-Module-Function&Class&Virable
#在包的目录下必须包含__init__.py文件，可为空文件
#可以有多级的包目录 test/test/.../test
#要注意，不能和python自带的模块名称冲突
f=test_module.test
print("1.",f)
print("2.",end=' ')
f()

g=test_module.greeting
print("3.",g('kql'))
print("4.",g("kqllifetime"))
#python的机制无法完全避免私有元素的访问
#所以，原则上，不应该访问这些元素
print("5.",test_module._private_1('kql'))


#模块文件的搜索目录：
#当前目录，已安装的内置模块和第三方模块目录--保存在sys.path中
#以及系统的环境变量PYTHONPATH--会被自动添加到搜索路径中

import sys
print("6.",sys.path)

