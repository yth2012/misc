import socket
import threading

url = "127.0.0.1"
port = 60065

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("socket err")
    exit(1)

try:
    soc.connect((url,port))
except:
    print("conn err")


try:
    soc.send(b"hello")
except:
    print("send chat err")

data = soc.recv(4096).decode()
print(data)








