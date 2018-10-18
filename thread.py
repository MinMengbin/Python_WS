# this is a file for python threading project

# usage: python3 thread.py

import threading
import time

def fun1():
    for i in range(1,10):
        time.sleep(1)
        print('i is ',i)

def fun2():
    for j in range(10,1,-1):
        time.sleep(1)
        print('j is ',j)

threading.Thread(target=fun1).start()
threading.Thread(target=fun2).start()
print(threading.active_count())