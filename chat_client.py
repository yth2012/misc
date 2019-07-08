import socket
import threading


def listenmsg():
    while 1:
        data = soc.recv(2048)
        if data:
            data = data.decode()
            print(data)

def listeninput():
    while 1:
        data = input()
        if data:
            soc.send(data.encode())


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

t1 = threading.Thread(target=listenmsg)
t2 = threading.Thread(target=listeninput)
t1.start()
t2.start()






