
def main():
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

if __name__=='_main_':
        main()