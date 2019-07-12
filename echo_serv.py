import asyncore
import time

class echo_serv(asyncore.dispatcher):
        def __init__(self,port):
                asyncore.dispatcher.__init__(self)
                self.host = "127.0.0.1"
                self.port = port
                self.create_socket()
                self.set_reuse_addr()
                self.bind((self.host,self.port))
                self.listen(5)

        def handle_accepted(self,sock,addr):
                print("conn from {}".format(addr))
                handler = echo_handle(sock,addr)

class echo_handle(asyncore.dispatcher_with_send):
        def __init__(self,addr):
                asyncore.dispatcher_with_send.__init__(self)
                self.addr = addr

        def handle_read(self):
                data = self.recv(4096)
                if data:
                        data = bytes(self.addr,encoding="utf-8") + data
                        ##self.broadcast(data)

        


if __name__ == "__main__":
        es = echo_serv(60065)
        asyncore.loop()

                



