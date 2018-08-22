# -*- coding:utf-8 -*-

import itertools

def pi(n):
    it_odd=itertools.count(start=1,step=2)
    fs=itertools.takewhile(lambda x:x<2*n,it_odd)
    sum,i=0,0
    for n in list(fs):
        #print(n)
        sum+=(-1)**i*4.0/n
        i+=1
    return sum

if __name__=='__main__':
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04<pi(10)<3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')
