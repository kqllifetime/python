#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#高阶函数，返回函数，匿名函数，装饰器，偏函数



#1.高阶函数 Higher-order function
#函数名也是变量，指向函数代码
fabs=abs
print("1.",fabs(-12),type(fabs),fabs.__name__)

#函数作为变量，传入某个函数当做参数，即是高阶函数
#函数的参数，是变量，这个变量是另一个函数
def abs_add(x,y,f=abs):
    return f(x)+f(y)
print("2.",abs_add(-10,-28,abs),abs_add(19,-11))

#内置函数：map/reduce,filter,sorted
from collections.abc  import Iterator
def f(x):
    return x*x
r=map(f,[1,2,3]) 
#传入函数f和一个Iterabble，
# 将f作用于Iterable对象的每一个元素，
#并返回一个Iterator 对象
print("3.",list(r),isinstance(r,Iterator))

from functools import reduce
DIGIT={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
def char2num(s):
    return DIGIT[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print("4.",str2int('12588'),type(str2int('1')),type(int(1)))


#用filter()函数求素数
#计算素数的一个方法是埃氏筛法
def odd_iter():#构建奇数数列，除了2，其他偶数都不是素数
    n=1
    while True:
        n=n+2
        yield n

def not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it=odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(not_divisible(n),it)

print("5.",end=' ')
for n in primes():
    if n <50:
        print(n,end=' ')
    else:
        break
print()


#sorted函数
#sorted(Iterable,key=,reverse=)->List
print("6.",sorted([3,5,-4,-9]))
print("7.",sorted([3,5,-4,-9],key=abs))
print("8.",sorted(['bob', 'about', 'Zoo', 'Credit']))
print("9.",sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print("9.",sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#2.返回函数
#闭包closure
#生成并返回函数，类似函数生成式，动态变化的函数体
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,2,3,4,5)
f1=lazy_sum(1,2,3,4,5)
print("10.",f(),f,f==f1)

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)  #只传入函数，函数内部的代码并未执行
    return fs
c1,c2,c3=count()
#三个返回函数的调用结果值都为9,因为fs.append(f)的f中引用了i
#当调用函数时，i都已经变为3，所以调用结果都为9
#所以，返回函数不要引用任何循环变量，或者后续会发生变化的变量
print("11.",c1(),c2(),c3())

#改进版本
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i)) #传入时，i已经确定，被传入函数中
    return fs
cc1,cc2,cc3=count1()
print("12.",cc1(),cc2(),cc3())


#3.匿名函数 lambda
#不常使用的函数，可以使用匿名函数，一次行执行的函数代码

print("13.",list(map(lambda x:x*x,[1,2,3,4,5])))

f=lambda x:x*x  #匿名函数赋值于某个变量
print("14.",f(6),f)

def func(x,y):
    return lambda z: x*x+y*y+z #返回匿名函数
print("15.",func(3,5)(1))


#4.装饰器 decorator: 可用于函数和类
#在原函数的功能不改变的前提下，增加新的功能和代码，又不影响原函数
#在代码运行期间动态增加功能的方式--装饰器Decorator

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print("2020-03-27")
print("16.",now)
now()

#5.偏函数 partial-function
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
import functools
int2=functools.partial(int,base=2)
    #相当于 def int2(s,base=2): return int(s,base)
print("17.",int2)
print("18.",int2('1000'),int2('1000',base=8))

