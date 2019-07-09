import socket
import time
import threading


host = "127.0.0.1"
port = 60065

def echo():
    while 1:
        data = conn.recv(2048)
        if data:
            print("recv data")
            ad = str(addr[0])
            msg = b"ad: " + data
            conn.send(msg)

def auto():
    while 1:
        time.sleep(3)
        conn.send(b"auto send")

s = socket.socket()
s.bind((host, port))

s.listen()
conn, addr = s.accept()

t1 = threading.Thread(target=echo)
t2 = threading.Thread(target=auto)
# t1.start()
t2.start()



