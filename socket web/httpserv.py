import os
import socket
import select


class server():
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        self.conns = {}
        self.sock = None
        s = socket.socket()
        s.bind((self.host,self.port))
        self.sock = s
        self.sock.listen(5)
        self.serv_4ever()

    def acc_conn(self):
        sock, addr = self.sock.accept()
        self.conns[addr[0]] = sock

    def serv_4ever(self):
        self.acc_conn()
        rready, wready, eready = select.select(self.conns.values(), [], [])

        for client_r in rready:
            req = ""
            while 1:
                buf = client_r.recv(1024)
                if buf:
                    req = req + buf.decode()
                else:
                    break
            if req:
                print(req)
                #self.handle_req(req)

        for client_w in wready:
            pass

    def handle_req(self, req):
        pass


if __name__ == "__main__":
    s = server()
    

