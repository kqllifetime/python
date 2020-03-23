#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#定义函数，函数参数，递归函数

#函数的作用：简化调用，代码复用，细节封装，代码抽象
#简化调用
r1=2
s1=3.14*r1*r1
def area_of_circle(PI,x):
    return round(PI*x*x,2)
print("1.",s1,area_of_circle(3.14,r1))#用函数调用代替细节代码
#代码复用,细节封装,代码抽象
r1=2
r2=3
r3=4
s1=3.14*r1*r1
s2=3.141*r2*r2
s3=3.1415*r3*r3
ss1=area_of_circle(3.14,r1) #代码通过函数调用实现复用，隐藏细节
ss2=area_of_circle(3.141,r2) #代码抽象：area_of_cirecl=>PI*r*r
ss3=area_of_circle(3.1415,r3)
print("2.",s1,s2,s3,"|",ss1,ss2,ss3)

#定义函数 
#def function(*args,**argkeys):
    #函数体部分，代码逻辑实现
    #return or no-return|none
def ff():
    pass #定义空函数
ff()     #空函数可以正常调用
import math
def quadratic(a,b,c):
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2    #返回多个值,返回tuple(x1,x2)
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

#函数的参数： 万能调用 func(*args,**kw)
#必选参数，默认参数，可变参数，命名关键字参数和关键字参数
#必选参数和默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print("1.",power(3,3),power(3))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print("3.")
enroll('Sarah', 'F')
print("4.",)
enroll('Bob', 'M', 7) #7对应age,city为默认
print("5.",)
enroll('Adam', 'M', city='Tianjin')#age为默认，city参数需要把参数名带上

#默认参数的坑-->默认参数必须指向不变对象
def add_end(L=[]):  #默认参数在定义是已经被计算出来了，也是变量，指向对象[]
    L.append('END')
    return L
print("6.",add_end())
print("7.",add_end()) #第二次调用，内容与第一次调用结果不一样

#修改后版本
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print("8.",add_end())
print("9.",add_end())


#可变参数：*args   函数调用时组装成一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print("10.",calc(),calc(1),calc(1,2))
nums=[1,2,3]
print("11.",calc(nums[0],nums[1],nums[2]),calc(*nums))

#关键字参数：
def person0(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print("12.",end=" ")
person0('Michael', 30)
print("13.",end=" ")
person0('Bob', 35, city='Beijing')
print("14.",end=" ")
person0('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
print("15.",end=" ")
person0('jack',24,**extra)

#命名关键字参数
#限定关键字参数，调用时必须全给出关键字参数名+值
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)
print("16.",end=" ")
person1('Jack', 24, city='Beijing', job='Engineer')#city和job缺一不可
print("17.",end=" ")
person1('Jack', 24, 1,city='Beijing', job='Engineer')

def person2(name, age, *, city='Beijing', job):#设定默认值
    print(name, age, city, job)
print("18.",end=" ")
person2('Jack', 24, job='Engineer')#可以不给出city
print("19.",end=" ")
person2('Jack', 24,city='Tianjin', job='Engineer')


#参数组合
#参数定义顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
print("20.",end=" ")
f1(1,2)
print("21.",end=" ")
f1(1,2,3)
print("22.",end=" ")
f1(1,2,3,4,5,6)
print("23.",end=" ")
f1(1,2,3,d=4)

print("24.",end=" ")
f2(1,2,d=0)
print("25.",end=" ")
f2(1,2,3,d=1)
print("26.",end=" ")
f2(1,2,d=2,e=4,f=5)

#特别的：给一个tuple和dict
args=(1,2,3,4)
kw={'d':10,'x':'#'}
print("27.",end=" ")
f1(*args,**kw)

args=(1,2,3)
kw={'d':11,'y':"!"}
print("28.",end=" ")
f2(*args,**kw)

#递归函数：函数在内部调用自身本身
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print("29.",fact(5)) 
print("30.",fact(100)) #递归调用的次数过多，会导致栈溢出

#递归优化--尾递归
#函数返回的时候，调用自身本身，return语句不能包含表达式
#尾递归调用，都只占用一个栈帧，不会出现栈溢出的情况
#目前python并不支持尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print("31.",fact(6))




#总结：
#默认参数：根据变动的频率，变动大的往前排，变动小的往后排
#可变参数：传入的参数被组装成一个tuple，可直接传入tuple,*args
#命名关键字：限定传入的关键字参数，必须给出关键字+值
#关机字参数：传入的参数被组装成一个dict，可直接传入dict,**kw

