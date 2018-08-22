# -*- coding:utf-8 -*-

import socket,os,threading
def tcp_threading():
    for i in range(1000):
        t=threading.Thread(target=tcp_client,name='thread'+str(i))
        t.start()

def tcp_client():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'michanel',b'tracy',b'sarach']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__=='__main__':
    #tcp_client()
    tcp_threading()
