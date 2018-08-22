# -*- coding: utf-8 -*-

def by_name(t):
    return t[0]


def by_value(t):
    return t[1]




L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2=sorted(L,key=by_name)
L3=sorted(L,key=by_value,reverse=True)
print(L2)
print(L3)
