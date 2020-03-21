#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#1.dict的操作

#创建:dict(),setdefault,fromkeys
d=dict()
d['a']=1
d0=dict([('b',2),('d',4)])
d0.setdefault('b',3)
d0.setdefault('c',3)
d1=dict(a=1,b=2,c=3,d=4,e=5)
d2={'a':1,'b':2,'c':3,'d':4}
d3=dict.fromkeys(['a','b'],[1,2])
print(d,d0,d1,d2,d3)

#删除：pop,popitem,clear,del

d1.pop('a')     #删除对应的key:值
d1.popitem()    #随机删除一个key:值
print("1.",d1,d1.popitem())

dd1=d1
d1.clear()
print("2.",d1,dd1)
del dd1
#print("3.",dd1)

#修改：dict['name']='what'; update
d2['d']=5
print("3.",d2)
d2.update({'d':6})
print("4.",d2)
d2.update(d=7)
print("5.",d2)

#查找：get(),dict['name'],in,keys,values,items,长度len
print("6.",len(d2))
print("7.",d2.get('d'),d2['d'])
print("8.",d2.keys())
print("9.",d2.values())
print("10.",d2.items())
print("11.",str(d2))

#拷贝：浅拷贝和深拷贝，copy,deepcopy
dd2=d2.copy()
print("12.",d2,dd2)
dd2['a']=10             #简单结构的复制和修改后，对原来的字典不影响
print("13.",d2,dd2)

dd2['a']=[1,0]
dd3=dd2.copy()
print("14.",dd2,dd3)
dd3['a'][0]=0           #复杂结构的复制和修改后，会影响原来的字典
print("15.",dd2,dd3)



#2.set的操作

#创建:只有key没有value，key须为不可变对象，set元素不重复，原理与dict类似
s1=set([1,2,3,4,5,3,4,2,1])
s2=set("helloworld")
print("\n",s1,s2,"\n")

#操作符：$,|,-,^
s3=set([3,4,5,6,7])
print("16.",s1&s3)
print("17.",s1|s3)
print("18.",s1-s3)
print("19.",s1^s3)
#操作符对应方法：intersection,union,difference,symmetric_difference
#更新原来的集合对象,intersection_update,difference_update,symmetric_differecnce_update
print("20.",s1.intersection(s3)) #对应s1&s3
print("21.",s1.union(s3))        #对应s1|s3
print("22.",s1.difference(s3))   #对应s1-s3 
print("24.",s1.symmetric_difference(s3)) #对应s1^s3
#判断关系：issubeset,issuperset,isdisjoint

print("25.",(s2&s3).issubset(s2))   #是否是s2的子集
print("26.",(s2|s3).issuperset(s2)) #是否是s2的父集
print("26-1.",(s2^s3).isdisjoint(s2&s3))   #是否没有交集

#增删查复制：add,update,remove,discard,pop,clear,len,in,copy
print("27.",s3)
s3.add(8)
s3.remove(7)
print("28.",s3)
s3.pop()
print("29.",s3)
s3.update([8,9])
print("30.",s3)
print("31.",len(s3))
print("31-1.",4 in s3)
print("31-2.",5 not in s3)
s4=s3.copy()
s3.clear()
print("32.",len(s3),s4)
s4.discard(9)
print("33.",s4)



