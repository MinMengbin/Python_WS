# this is a file for python threading project
# Author: Mike Min 
# Email: msner10010@hotmail.com

# usage: python3 _main_.py

import threading as pcthread  #class for multithreading
import time
import logging as log1
import random as rand_num

thread_num = 0 # thread number


# Func: a logge function without arguments
def funclog():
        logger1 = log1.getLogger()
        logger1.warning('A logging thread is running')

# Func: a logge function with arguments
def funclogarg(arg1, arg2, arg3):
        global thread_num
        thread_num = thread_num + 1
        logger2 = log1.getLogger()
        t_sleep = rand_num.randint(1,5)
        print ('The sleep time of thread',thread_num,'is:',t_sleep)
        time.sleep(t_sleep)
        logger2.warning('Arguments for this logger function are %d, %d, %d', arg1, arg2, arg3)

#Func: a fuction to get a close result to the root of a number 
def rootofn(n_input):
        ''' Calculates the square root of n_input '''
        eps = 0.0000001
        old = 1
        global new 
        new = 1
        while True:
                old, new = new, (new + n_input/new) / 2.0
                # print(old, new)
                if abs(new - old) < eps:
                        break
        return new

# Func: a simple function called fun1()
def fun1():
    for i in range(1,10):
        time.sleep(1)
        print('i is ',i)

# Func: a simple function called fun2()
def fun2():
    for j in range(10,1,-1):
        time.sleep(1)
        print('j is ',j)

def main():
        print ('Main function is running')
        # pcthread.Thread(target=fun1).start()
        # pcthread.Thread(target=fun2).start()

        '''Coding: thread of passing inputs and outputs'''
        # global n1
        # n1 = int(input("Enter a number: "))
        # root_thr = pcthread.Thread(target = rootofn, args = (n1,))
        # root_thr.start()
        # root_thr.join()
        # print ('the root of',n1,'is',new)

        '''Coding: thread of logger'''
        ## a case
        # logger_thr = pcthread.Thread(target = funclog, name='thread_logger')
        # logger_thr.start()
        # logger_thr.join()
        ## a case
        # loggeragr_thr = pcthread.Thread(target = funclogarg,name='thread_logger',args=(1,2),kwargs={'arg3': 3})
        # loggeragr_thr.start()
        # loggeragr_thr.join()
        ## a case
        for i in range(1,10):
                loggeragr_thr = pcthread.Thread(target = funclogarg,name='thread_logger',args=(1,2),kwargs={'arg3': i})    
                loggeragr_thr.start()
        #loggeragr_thr.join()

        # print(pcthread.active_count())