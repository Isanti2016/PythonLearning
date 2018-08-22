#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun(l):
    for s in l:
        if isinstance(s,str)==True:
            print(s.lower())
        else:
            print('is not a charater')

l=['Hello','World','Apple','None']
fun(l)

l=['Hello','World',18,'Apple','None']
fun(l)
