def gen1():
    print("its gen1")
    yield 1

def gen2(i):
    print("its 2")
    for o in i:
        yield o + 1

def gen3(i):
    print("its 3")
    for o in i:
        yield o + 1

def genrecv():
    print("gen recv")
    i = 0
    while i < 5:
        recv = yield
        print(recv)
        i += 1

def gen4():
        for i in range(5):
                yield i

if __name__ == "__main__":
''' mygen = gen1()
    mygen2 = gen2(mygen)
    mygen3 = gen3(mygen2)
    for o in mygen3:
        print(o)
'''
        g = gen4()
        for o in g:
                print(i)
