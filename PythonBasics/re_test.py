# -*- coding:utf-8 -*-

import re

def verification_email(test):
    re_email=re.compile(r'([<>\s\wa-z0-9.]+)@([a-z0-9]+).([a-z]{3})')
    grp=re_email.match(test)
    if grp:
        print('correct email address')
    else:
        print('wrong email address')


if __name__=='__main__':
    verification_email('bill.gates@microsoft.com')
    verification_email('<Tom Paris>tom@voyager.org')


