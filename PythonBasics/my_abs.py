#!/usr/bin/env python
# -*- coding: utf-8 -*

num=input("input number:")
x=int(num)

def my_abs(x):
    if not_isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x
print("abs of number:%d" % x)
