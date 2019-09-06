import os

def fun1():
    print("from func 1")
    os.fork()

def fun2():
    print("from func 2")


if __name__ == "__main__":
    fun1()