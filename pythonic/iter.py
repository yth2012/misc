class node():
    def __init__(self, value):
        self.value = value
        self.nextone = None

    def getvalue(self):
        return self.value

    def setnext(self, nextnode):
        self.nextone = nextnode

    def getnext(self):
        return self.nextone

    def __iter__(self):
        return nodeiterator(self)

class nodeiterator():
    def __init__(self, node):
        self.start = node

    def __next__(self):
        now = self.start
        if now:
            self.start = now.getnext()
            return now.value
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self

if __name__ == "__main__":
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    n1.setnext(n2)
    n2.setnext(n3)
    t1 = n1.__iter__()
    for i in range(4):
        try:
            print(t1.__next__())
        except StopIteration:
            print("reach")

