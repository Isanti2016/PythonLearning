# -*- coding:utf-8 -*-

import hashlib
import functools
from collections import defaultdict

def add_salt(salt='the-salt'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            args2=list(args)
            args2[0]+=salt
            return func(*args2,**kw)
        return wrapper
    return decorator

@add_salt()
def get_md5(s):
    md5=hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

#无装饰器
#def md5_salt(s,salt='the-salt'):
#    return get_md5(s+add_salt())

db=defaultdict(lambda:'不存在')

def register():
    global db
    name=str(input('请输入账号:'))
    pwd=str(input('请输入密码:'))
    db[name]=get_md5(name+pwd)

def login():
    username=str(input('请输入账号：'))
    password=str(input('请输入密码：'))
    md5=get_md5(username+password)
    if db[username]==md5:
        print('登录成功')
    else:
        print('登录失败')


if __name__=='__main__':
    while True:
        print('1.注册')
        print('2.登录')
        print('3.退出')
        x=int(input('请选择：'))
        try:
            if x==3:
                break
            elif x==2:
                login()
            elif x==1:
                register()
            else:
                print('输入有误，请重新输入')
        except ValueError as k:
            print('输入非法,请重试：')

#if __name__=='__main__':
#    while True:
#        cd={
#            '1':register,
#            '2':login
#        }
#        print('1.注册\n2.登录\n3.退出')
#        x=int(input('请选择：'))
#        if x==3:
#            break
#        try:
#            cd[str(x)]
#        except KeyError as k:
#            print('输入有误，请重新输入')
