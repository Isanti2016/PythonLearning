#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def hello(greeting,*args):
    if(len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting,','.join(args)))

hello('hi')
hello('hi','sarah')
hello('hello','michael','bob','adam')

names=['bart','lisa']
hello('hello',*names)


def print_scores(**kw):
    print('    Name Score')
    print('--------------')
    for name,score in kw.items():
        print('%10s  %d' % (name,score))
    print()
print_scores(Adam=90,lisa=44,bart=77)

data={
    'adam lee':99,
    'lisa s':88,
    'F,Bart':87
}
print_scores(**data)

def print_info(name,*,gender,city='beijing',age):
    print('Personal Info')
    print('-------------')
    print('  Name:%s' % name)
    print('Gender:%s' % gender)
    print('  City:%s' % city)
    print('   Age:%d' % age)
    print()

print_info('Bob',gender='male',age=20)
print_info('lisa',gender='female',city='shanghai',age=18)

