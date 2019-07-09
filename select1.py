import socket
import sys
import select

s = socket.socket()


s.connect(("127.0.0.1", 60065))
input = [sys.stdin, s]


while 1:
    
    iready, oready, eready = select.select(input,[],[])
    for i in iready:
        if i is sys.stdin:
            msg = sys.stdin.readline()
            s.send(msg)

        elif i is s:
            data = s.recv(2048).decode()
            print(data)