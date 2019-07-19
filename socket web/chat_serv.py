import socket
import threading
import sys

class server():
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 60065
        self.pool = {}
        self.count = 0
        self.sock = None

    def init_serv(self):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.bind((self.host,self.port))
            self.sock.listen(50)
            while 1:
                self.handle_conn()
        except :
            print("socket err from serv")

    def client_tunnel(self,conn,addr):

        while 1:
            try:
                msg = conn.recv(2048).decode()
                msg = bytes(addr[0] +  " : " + msg, encoding="utf-8")
                self.broadcast(msg,conn,addr)
            except:
                print("client tunnel err")

    def broadcast(self, msg, conn, addr):

        for client in self.pool.values():
            if client != conn:
                try:
                    client.send(msg)
                except:
                    print("err broadcast")

    def handle_conn(self):
        
        try:
            conn, cli_addr = self.sock.accept()
            self.pool[cli_addr[0]] = conn
            print("got conn from {}".format(cli_addr[0]))
            conn.send("connected".encode())
            t = threading.Thread(target=self.client_tunnel, args=[conn,cli_addr])
            t.start()
            
            
        except:
            e = sys.exc_info()
            print(e[0])

    
            

if __name__ == '__main__':
    s = server()
    s.init_serv()
