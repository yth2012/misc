import sys
import socket

class haha():
    def __init__(self):
        self.x = 1
        self.y = 2

    def one(self):
        self.two()
        print("one")

    def two(self):
        print("two")

    
if __name__ == '__main__':
    h = haha()
    h.one()