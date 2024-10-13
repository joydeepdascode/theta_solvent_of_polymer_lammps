#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:35:52 2021

@author: joy
"""

from numpy import linspace,arange,empty,array,zeros,append,insert,ones


x=array([1])

#x=x.append([2])

x=linspace(1,10,10)
x=arange(1,10,1)
x=append(x,[11,22])
a=[]
a.append([[1,23],[3]])
print(a)
print('dim')
print(x.ndim)

print(x.shape)
print(x.size)

p=zeros(20).reshape(4,5)
print(p)

print('##################\n\n')


q=zeros(3)

q=3+q


print(q)

print('#########qqqqqqqqq#######\n\n')

x=linspace(0,5,6)
di=ones(6)
di=di+x
print(di)

"""
n=int(input('Enter number of atoms '))

print(str(n))


xlo=float(input('Enter x low value '))
xhi=float(input('Enter x high value '))
print(str(xlo))
print(str(xhi))

"""

#mk=float(input('enter the value '))
#print(str(mk+6))
#s=mk+0.1
#print(str(s))
print("###############-----------######")

a=1
for i in range(1,int(a)+1):
    print(i)



