import os
import socket


class broken_server():

    def __init__(self, addr, port, req_handl):
        self.socket = socket.socket()
        self.address = addr
        self.port = port
        self.socket.bind((self.address, self.port))
        self.handler = req_handl

    def listen(self):
        while 1:
            self.socket.listen()
            conn, addr = self.socket.accept()
            return (conn, addr)
            
    def handle_req(self, conn):
        self.handler(self, conn)

    def serve(self):
        conn, addr = self.listen()
        self.handle_req(conn)



class request_handler():

    def __init__(self, serverinstance, connection):
        self.server = serverinstance
        self.conn_r = connection.makefile('rb')
        self.conn_w = connection.makefile('wb')
        self.handle()
        self.close()

    def handle(self):
        
        req = self.conn_r.readline(65535)

        if req:
            req = req.decode()
        else:
            req = ""

        self.conn_w.write(bytes("you enter {}".format(req), encoding="utf-8"))
        return
        
    def close(self):
        self.conn_r.close()
        self.conn_w.close()

    def parse_req(self, req):
        reqline = req.split('\r\n')


if __name__ == "__main__":
    s = broken_server('127.0.0.1', 60065, request_handler)
    s.serve()