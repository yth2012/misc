import threading
import time
import random
import concurrent.futures

def thread_func(iid,idid):
    print("thread {} is running".format(iid))
    idid += 1
    time.sleep(random.randint(0,3))
    print("thread {} finish".format(iid))

if __name__ == '__main__':
    '''pool = concurrent.futures.ThreadPoolExecutor()
    pool.map(thread_func,range(3))'''
    for i in range(3):
        t = threading.Thread(target=thread_func, args=[i,i])
        t.start()
        