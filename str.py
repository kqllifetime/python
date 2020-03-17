#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#python中的字符串和编码

#字符串在内存中是以Unicode编码的
print('这是一个str编码的例子')
#ord()函数获取字符的整数表示
print('1.',ord('A'))
print('2.',ord('中'))
#chr()函数把编码转换为对应的字符
print('3.',chr(66))
print('4.',chr(25991))
print('5.',chr(ord('A')))
#十六进制的字符
print('6.','\u4e2d\u6587')
#字节类型的字符-encode+decode
#内存中用unicode编码，存储和传输用utf-8(兼容ascii编码)
print('7.',b'ABC')
print('8.','ABC'.encode('ascii'))
print('9.','中文'.encode('utf-8'))
print('10.',b'ABC'.decode('ascii'))
print('11.',b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('12.',b'\xe4\xb8\xad\xe6'.decode('utf-8',errors='ignore'))
#字符串的长度-len()函数：计算str的字符数,计算bytes的字节数
print('13.',len('abc'))
print('14.',len('中文'))
print('15.',len(b'abc'))
print('16.',len('中文'.encode('utf-8')))
#字符串的格式化-%和format,format_map
print('17.','%2d-%02d' % (3, 1))
print('18.','%5.2f%%' % 3.1415926)
print('19.','Hello,{0},welcome,{1:.3f}'.format('kql',0.5201))
student={'name':'小明','class':'20190301','score':597.5}
print("19-1.",'{st[class]}班{st[name]}总分：{st[score]}'.format(st=student))
print("19-2.",'{class}班{name}总分：{score}'.format_map(student))
##字符串的常规操作
#包括：编码，转码，格式，输出，输入，下标，切片，连接，去除空格
#       查找，比较，包含，长度，大小写转换，插入，统计，测试，判断
#       分割，替换，切割等等
#1.字符串的连接
#join,+
print("20.",'a'+'b')
print("20-1.",'+'.join('abcdef'),'-'.join(['1','2','3']))
#2.字符串的截段切片
print("21.",'abcdefg'[2:6])
#3.字符串的大小写转换
print("22.",'abCD'.lower()) 
print("23.",'abCD'.upper())
print("24.",'abc def ghi'.title())
print("25.",'abc def ghi'.capitalize())
print("26.",'abCD'.swapcase())
print("26-2.",'ß'.casefold())
#4.字符串测试和判断函数
#isalpha,isdecimal,isdigit,isnumeric,isalnum,isascii
print("27.",'abc'.isalpha())
print("28.",'abc21'.isalnum())
print("29.",'123'.isnumeric())
print("30.",'123'.isdecimal())
print("31.",'123'.isdigit())
print("31-2.",'123'.isascii())
print("31-3.",'中'.isascii())

#islower,isupper,istitle
print("32.",'abc'.islower())
print("33.",'ABC'.isupper())
print("34.",'Abc'.istitle())
#isspace,isprintable,isidentifier
print("35.",''.isspace())
print("36.",'\n'.isprintable())
print("37.",'2abc'.isidentifier())
#5.填充
#center,ljust,rjust,zfill
print("38.",'ab'.center(5,'+'))
print("39.",'abcde'.center(3,'+'))
print("40.",'ab'.center(5))
print("41.",'ab'.ljust(5,'+'))
print("42.",'ab'.rjust(5,'+'))
print("43.",'ab'.zfill(5))
print("44.",'-12'.zfill(5))
#6.子串搜索
#count,endswith,startswith,find,rfind,index,rindex,in
print("45.",'abcaabcdec'.count('a'))
print("46.",'abcaabcdec'.count('a',1))
print("47.",'abcaabcdec'.count('a',1,4))
print("48.",'abcxyz'.endswith('xyz'))
print("49.",'abcxyz'.endswith('xyz',4))
print("49.",'abcxyz'.endswith('xyz',0,5))
print("50.",'abcxyz'.endswith(('ab','xyz')))
print("51.",'abcxyz'.startswith('ab'))
print("52.",'abcxyzXY'.find('xy'))
print("53.",'abcxyzXY'.find('xy',4))
print("54.",'abcxyzXYbc'.find('bc'))
print("55.",'abcxyzXYbc'.rfind('bc'))
print("56.",'abcxyzXYbc'.index('yz',2))
print("57.",'abcxyzXYbc'.rindex('bc',2))
print("58.",'ab' in 'bcadeab')
#7.替换
#replace,expandtabs,translate & maketrans

#8.分割
#partition & rpartition,split & rsplit & splitlines


#9.修剪
#strip,lstrip,rstrip
