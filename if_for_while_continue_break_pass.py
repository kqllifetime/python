#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#1.if 选择语句
#if,elif,else
height=1.75
weight=80.5
res=''
bmi=weight/(height*height)
if bmi<18.5:
    res="过轻"
elif bmi<25:
    res="正常"
elif bmi<28:
    res="过重"
elif bmi<32:
    res="肥胖"
else:
    res="严重肥胖"
print("1.",res)

#2.循环语句：for,while,contiue,break,range,pass
#for循环
sum=0
for x in range(101):
    sum=sum+x
print("2.",sum)

names = ['Michael', 'Bob', 'Tracy']
print("3.",end=' ')
for name in names:
    print(name,end=' ')
print()
print("4.",res,res,res,sep='|',end='!\n') #print的两个参数sep和end

num=0
for x in range(1,51):
    if x/2/3/4!=1:
        continue
        # pass
    else:
        num=x
        break
    print('没法执行我')
print("5.",num)

#while循环

num=0
x=1
while num==0:
    if x/3/4/5!=1:
        x=x+1
        #continue
    else :
        num=x
        #break
    
print("6.",num)   