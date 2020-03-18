#!/usr/bin/env python
# -*- coding: utf-8 -*-
a=[1,2,3,4,5] #[]-list,有序，可变
b=(1,2,3,4,5,) #()-tuple，有序，不可变
c=['abc',123,True]
d=[['a','b','c'],'abc',321,(1,2,3)]
print(a)
print(b)
print(c)
print(d)

#1.list的常规操作
print('1.',len(a))
print('2.',a[1])
print('3.',a[len(a)-1])
print('4.',a[-1])
print("5.",a[-2])
print("5-1.",a[0:3])
print("5-2.",a[-3:])
print("5-3.",a[:-3])

a.append(6)     #末尾添加元素
print("6.",a)

a.insert(1,0)   #指定index位置插入元素
print("7.",a)

a.pop()         #pop()删除末尾元素，pop(i)删除指定位置元素
print("8.",a)

a.pop(1)
print("9.",a)

a[0]=0;a[-1]=6          #修改某元素，直接通过索引赋值
print("10.",a)

del a[-1]       #删除某元素
print("11.",a)

a1=a+[5]        #+,组合元素
print("12.",a1)

a2=a+[1]*2      #×，重复元素
print("13.",a2)

print("14.",3 in a) #判断元素是否存在于列表中
for x in a : print(x)   #list元素迭代

print("15.",max(a))     #返回列表的最大值
print("16.",min(a))     #列表的最小值
print("17.",list(b))    #把tuple转换成列表

print("18.",a.count(2)) #统计某个元素在列表中出现的次数
print("19.",a.index(3)) #从列表中找出某个值第一个匹配项的索引位置

a3=a+[7]*2
print("20.",a3)
a3.remove(7)        #移除列表中某个值的第一个匹配项
print("21.",a3)

a4=a.copy()         #复制列表，新的内存空间
a5=a
print("22.",id(a4),id(a),id(a5))

a6=a.copy()
print("23.",a6)
a6.clear()          #清空列表
print("24.",a6)

a7=a.copy()     
a7.extend('89')     #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print("25.",a)
print("26.",a7)

a8=a                #改变a8的同时，a指向的值也改变了
a8.extend('abc')    #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print("27.",a,a8)

a9=[1,2,3,5,4,7,8,6]
a9.reverse()    #反转列表中元素顺序
print("28.",a9)
a9.sort()       #对列表元素进行排序，默认升序reverse=False
print("29.",a9)
a9.append(2)
a9.sort(reverse=True)   #降序排列输出
print("30.",a9)
a9.sort()

# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1] 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)] 
# 指定第二个元素排序
random.sort(key=takeSecond) 
# 输出类别
print ('排序列表：', random)
