import asyncore
import asynchat

room = {}

class echo_serv(asyncore.dispatcher):
        def __init__(self,port):
                asyncore.dispatcher.__init__(self, map=room)
                self.host = "127.0.0.1"
                self.port = port
                self.create_socket()
                self.set_reuse_addr()
                self.bind((self.host,self.port))
                self.listen(5)

        def handle_accepted(self,sock,addr):
                print("conn from {}".format(addr))
                
                handler = echo_handle(sock,addr)

class echo_handle(asynchat.async_chat):
        def __init__(self,sock,addr):
                asynchat.async_chat.__init__(self,sock=sock)
                self.set_terminator('\n')
                self.addr = addr
                self.msg = []

        def collect_incoming_data(self,data):
                self.msg.append(data)

        def found_terminator(self):
                msg = "".join(self.msg)
                for client in room.values:
                        client.push(self.msg + '\n')
                self.msg = []



if __name__ == "__main__":
        es = echo_serv(60065)
        asyncore.loop(map=room)

                



