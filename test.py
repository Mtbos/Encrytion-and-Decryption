import os
import sys
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input('Enter ip:')
port = int(input('port:'))
while True:
    s.connect((ip, port))
    print('listening..')
    connection = True
    if connection is True:
        b = sys.argv[0]
        print(b)
        file = os.listdir()
        if file == '*.exe':
            file.remove('*.exe')
            print('removed')
        files = file.__len__()
        print(files)
        os.close(files)
    else:
        exit()