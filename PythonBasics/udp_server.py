# -*- coding:utf-8 -*-

import socket

def udp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',9999))

    print('Bind UDP ON 9999...')
    while True:
        data,addr=s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello,%s!' % data,addr)


if __name__=='__main__':
    udp_server()
