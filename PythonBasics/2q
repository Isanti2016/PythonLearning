# -*- coding: utf-8 -*-

from functools import reduce

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('123'))


def normalize(l):
    def fun(name):
        return name[0].upper()+name[1:].lower()
    return map(fun,l)

L1 = ['adam', 'LISA', 'barT']
L2=list(normalize(L1))
print(L2)

def prod(l):
    def fun(x,y):
        return x*y
    return reduce(fun,l)

l=[3,5,7,9]
print('3*5*7*9=',prod(l))

def str2float(s):
    def fun(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    n=s.index('.')
    s1=list(map(char2num,[x for x in s[:n]]))
    s2=list(map(char2num,[x for x in s[n+1:]]))
    return reduce(fun,s1)+reduce(fun,s2)/10**len(s2)

print('\'123.45678\'=',str2float('123.45678'))
