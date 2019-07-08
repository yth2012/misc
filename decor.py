def testing(func):
    def wrapper():
        print("this is top")
        func()
        print("this is bottom")

    return wrapper

@testing
def some():
    print("this is some")


if __name__ == "__main__":
    some()