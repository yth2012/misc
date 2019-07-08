import select
import socket

url = '127.0.0.1'
port = 60065

for i in range(3):
    s = socket.socket()
    s.connect((url,port))