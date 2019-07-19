import socket 

url = "www.baidu.com"
port = 80

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((url,port))

req = b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"

soc.send(req)
resp = ""
while True:
    res = soc.recv(1024)
    if res:
        resp = resp + res.decode()
    else:
        break

soc.close()

html = open("sockethtml.html", "w",encoding="utf-8")
if resp:
    html.write(resp)
else:
    print("no resp")
html.close()
