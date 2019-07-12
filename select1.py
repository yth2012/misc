import socket
import sys
import select

# s = socket.socket()


# s.connect(("127.0.0.1", 60065))
ip = [sys.stdin]
op = [sys.stdout]

while 1:
    ir, outr, errr = select.select(ip,op,[])
    if ir:
        data = sys.stdin.readline()
        print("you entersome")
    if outr:
        sys.stdout.flush()
