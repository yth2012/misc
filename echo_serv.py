import socket

host = "127.0.0.1"
port = 60065

s = socket.socket()
s.bind((host, port))

s.listen()
conn, addr = s.accept()
print(addr[0])
conn.send("hello".encode())