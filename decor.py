def testing(func):
    def wrapper():
        print("this is top")
        func()
        print("this is bottom")
    return wrapper

def wrap1(func):
    def wrapper(*args, **kwargs):
        print("doing this")
        func(*args,**kwargs)
        print("finishing")
    return wrapper

@testing
def some():
    print("this is some")

@wrap1
def some1(num):
    print(num + 1)


if __name__ == "__main__":
    some1(5)