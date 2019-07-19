import asynchat

host = '127.0.0.1'
port = 60065


class chatclient(asynchat.async_chat):
    def __init__(self):
        asynchat.async_chat.__init__(self)
        self.create_socket()
        self.connect((host,port))
        self.set_terminator('\n')
        self.msg = []
        self.icmsg = []

    def found_terminator(self):
        pass

    def handle_read(self):
        while 1:
            data = self.recv(2048)
            if data:
                self.icmsg.append(data)
            else:
                break












