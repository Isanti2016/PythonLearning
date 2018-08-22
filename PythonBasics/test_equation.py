#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i,(int,float)):
            raise TypeError("bad operand type")
    r=b**2-4*a*c
    if a==0:
        return "a=0,次方程是一元一次方程"
    if r<0:
        print("此方程无实数解")
    else:
        x1=(-b+math.sqrt(r))/(2*a)
        x2=(-b-math.sqrt(r))/(2*a)
        return x1,x2
a=float(input("请输入a的值，a="))
b=float(input("请输入b的值，b="))
c=float(input("请输入c的值，c="))
print(quadratic(a,b,c))


