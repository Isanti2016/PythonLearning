# -*- coding:utf-8 -*-

import functools


def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call')
            if text==None:
                print('call= %s:' % func.__name__)
            else:
                print('text=%s\ncall=%s' % (text,func.__name__))
            func(*args,**kw)
            print("end call")
            return func
        return wrapper
    return decorator

@log('123')
def fun():
    print('2017-11-12')
@log()
def fu():
    print('No args')
print(fun())
print(fu())

from functools import wraps
from time import time, sleep

start_time = time()
print("\n现在开始运行...\n\n**********************\n")

def log(text):
    def decorator(func):
        @wraps(func)
        def wrapers(*args, **kw):
            print("函数{0}()即将执行，此时系统已运行了 {1} 秒\n".format(func.__name__, time()-start_time))
            startTime =  time()
            return (func(*args, **kw),print("函数{0}()执行了 {1} 秒后，结束了自己\n".format(func.__name__, time()-startTime)))[0]
        return wrapers
    return (decorator,print("我是一个带参数的装饰器，我的参数是 '{}' ".format(text) ))[0] if text.__str__() == text else decorator(text)

@log
def abc():
    print("我是函数abc(),我正在执行中，不过我要睡 5 秒\n")
    sleep(5)

@log('嘿，伙计，是你吗？\n')
def efg():
    print("我是函数efg(),我正在执行中，我只想睡 3 秒\n")
    sleep(3)

abc()
efg()


print("运行结束，一共运行了",time()-start_time,"秒")
