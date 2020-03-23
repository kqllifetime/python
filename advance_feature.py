#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#高级特性
#切片，迭代，列表生成式，生成起，迭代器

#1.切片 slice
#切片可用于有序的数据类型，如：List,Tuple,Str
#切片使用索引对数据进行截取，生成并返回新的对象类型
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print("1.",L[0:2],L[:2],L[1:],L[2:4],L[::2],sep="\n")
print("2.",L[:2],L[-2:],L[:-1],L[:],sep="\n")

T = (0,1,2,3,4,5)
print("3.",T[:],T[:3],T[2:],T[-3:],T[::3],sep='\n')

S = 'ABCDEFG'
print("4.",S[1:4],S[:3],S[-2:],S[4:],S[1:6:2],S[:],sep='\n')

# def trim(s):
#     left_index=0
#     right_index=0
#     if s.isspace()==True or s=='':
#         return ''
#     for i in range(0,len(s)):
#         if s[i].isspace()==True:
#             continue
#         else : 
#             left_index=i
#             break
#     for i in range(1,len(s)):
#         if s[-i].isspace()==True:
#             continue
#         else:
#             right_index=len(s)-i
#             break
#     s=str(s[left_index:right_index+1])
#     return s
# def trim(s):  #找出左右的非空格字符的索引，然后s[b:e]
#     s_len = len(s) 
#     begin = end = s_len
#     for i, a in enumerate(s):
#         if a != " " and begin == s_len: 
#             begin = i
#         if a == " " and begin != s_len and s[i-1] != " ":
#             end = i
#     s = s[begin:end]
#     return s
# def trim(s): #删去左边空格，翻转，删去右边空格，再翻转
#     if s:
#         l = list(s)
#         n = 0
#         while n < 2:
#             if l[0] == " ":
#                 del l[0]
#                 if not l:
#                     return ""
#                 continue
#             l.reverse()
#             n += 1
#         return "".join(l)
#     else:
#         return ""
# def trim(n):  #递归

#     if n[:1] == ' ':

#         return trim(n = n[1:])

#     if n[-1:] == ' ':

#         return trim(n = n[:-1])

#     return n  
def trim(s):    
    #最简洁的写法：
    # 左边：s[0]/s[:1]是空格，切片[1:]，循环
    # 右边：s[-1]/s[-1:]是空格，切片[:-1]，循环
    # 最后：得到一个不包含空格的最终切片
    while s[-1:] == ' ':
        s = s[:-1]
    while s[:1] == ' ':
        s = s[1:]
    return s
print("5.",end=" ")
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')

#2.迭代 Iteration
#只要是Iterable(可迭代对象),都可以用for.in.进行迭代操作
#如：List,Tuple,Str,Dict,Set;数值不可迭代

#判断是否是可迭代对象 
from collections import Iterable
print("6.",isinstance('abc',Iterable))
print("7.",isinstance([1,2],Iterable))
print("8.",isinstance((1,2),Iterable))
print("9.",isinstance({1:2},Iterable))
print("10.",isinstance(set('abc'),Iterable))
print("11.",isinstance(123,Iterable))

#dict的迭代
#迭代key:for k in dict.keys()
#迭代value: for v in dict.values()
#同时迭代key和value：for k,v in dict.items()
d = {'a': 1, 'b': 2, 'c': 3}
print("12.",end=" ")
for k in d.keys():
    print(k,end=' ')
print()

print("13.",end=" ")
for v in d.values():
    print(v,end=' ')
print()

print("14.",end=' ')
for k,v in d.items():
    print("%s:%s"%(k,v),end=' ')
print()

#List，Tuple，Str，Set的迭代
L=[1,2,3,4,5]
T=(1,2,3,4,5)
S='12345'
Ss=set('12345')
LL=[L,T,S,Ss]

print("15.")
for i in LL:
    print(type(i),":",end=' ')
    for m in i:
        print(m,end=' ')
    print()

#enumerate函数：把一个list变成索引-元素对
print("16.")
for i,v in enumerate(['a','b','c']):
    print(i,v)


#3.列表生成式 List Comprehensions
#直接生成一个列表，列表的元素数量是有限的，因为受到内存限制
print("17.",list(range(1,11)))
print("18.",[x*x for x in range(1,11)])
print("19.",[x*x for x in range(1,11) if x%2==0])
print("20.",[m+n for m in 'ABC' for n in 'XYZ'])
d={'x':'A','y':'B','z':'C'}
print("21.",[k+'='+v for k,v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print("22.",[s.lower() for s in L])

#if在for前面为表达式,需要加else才完整，在for后面为筛选条件
print("23.",[x for x in range(1,11) if x%2==0])
print("24.",[x if x%2==0 else -x for x in range(1,11)])


#4.生成器：Generator
#一边循环一边计算出下一个元素，可生成无限数量的元素
#生成器，既是Iterable,也是Iterator
g=(x*x for x in range(10))
print("25.",g)
print("26.",end=' ')
for x in g:
    print(x,end=' ')
print()
#函数->生成器

def fib(max): 
    n, a, b = 0, 0, 1
    while n < max: #有限的斐波那契数列
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
def fib1():
    a, b =  0, 1
    while True: #无限的斐波那契数列
        yield b
        a, b = b, a + b
        

f=fib(6)
print("27.",f)
print("28.",end=' ')
for n in f:
    print(n,end=' ') #无法获得return的返回值
print()

g=fib(8)
print("29.",end=' ')
while True:
     try:
         x = next(g)
         print(x,end=' ')
     except StopIteration as e: #捕获错误，获取return返回值
         print(e.value)
         break
         #生成器迭代到最后，就无法再next了

gf=fib1()
print("30.",end=' ')
n=0
while n<15:
    x=next(gf)
    print(x,end=' ')
    n+=1
print()

#5.迭代器：Iterator
#可迭代对象Iterable：list,tuple,dict,set,str,generator
#迭代器Iterator: 可以作用与for循环，
#    也可以被next()函数不断调用返回下一个值，知道最后抛出StopIteration
#genarator既是Iterable，也是Iterator
#可以使用iter()函数，把list,dict,str等Iterable变成Iterator
from collections.abc import Iterator
print("31.",isinstance([],Iterable))
print("32.",isinstance(iter([]),Iterator))

# Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，
# 但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，
# 只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
# 而使用list是永远不可能存储全体自然数的
# Python的for循环本质上就是通过不断调用next()函数实现的