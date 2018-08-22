# -*- coding:utf-8 -*-

import struct,os

def check_bmp(path):
    with open(path,'rb') as f:
        info=struct.unpack('<ccIIIIIIHH',f.read(30))
        if info[0]==b'B' and info[1]==b'M':
            print('info：',info)
            print('是位图，大小为%s*%s,颜色数:%s' % (info[4],info[5],info[-1]))
        else:
            print('不是位图')


