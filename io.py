import threading
import time

def crawl():
    time.sleep(0.02)


def main1():
    for i in range(100):
        crawl()

def main2():
    tpool = []
    for i in range(100):
        t = threading.Thread(target=crawl)
        t.start()
        tpool.append(t)

    for t in tpool:
        t.join()

if __name__ == '__main__':
    s = time.time()
    main1()
    e = time.time()
    print("single thread: {:.6f}".format(e - s))
    s = time.time()
    main2()
    e = time.time()
    print("multi : {:.6f}".format(e -s))