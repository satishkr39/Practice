# multithreading demo in python
import time
import threading
import concurrent.futures

start = time.perf_counter()  # starting counter

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('sleep finished')

def do_something_with_arg(second):
    print(f'Sleeping for {second} second(s)')
    time.sleep(second)
    return f'sleep finished {second}'

# old ways of running process 1 by 1
# do_something()
# do_something()

# defining 2 threads and assigning them the task that needs to be executed. we've defined the thread only
# its not going to do anything. as we haven't asked the thread to start.
'''t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something_with_arg, args=['satish']) # passing args at time of defining thread
# to start the thread
t1.start()
t2.start()

# joins method makes sure that the thread is finished before moving ahead of this line
t1.join()
t2.join()
# below lines will only start when the thread are completed.
'''

'''
# running threads in for loop
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t) # we can't use t.join() here as it will stop for each thread before moving to next thread. so it won't be Thread at all.

# now it will wait untill all threads are completed and then it will move to next script.
for t in threads:
    t.join()
'''
'''
def sleep_second_by_user_input(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)
    print('sleep finished')

# calling parametrized method
t1 = threading.Thread(target=sleep_second_by_user_input, args=[1.5])
t1.start()
t1.join()
'''
# using Threading using concurrent.futures. running for 2 process manually
with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something_with_arg, 1) # calling parametrized method. passing 1 as args
    # f2 = executor.submit(do_something) # calling non-parametrized argument.
    #
    # # we can even prints the results of the method returned using the below codes. the method should return some values
    # print(f1.result())  # if it returns nothing then it will print None
    # print(f2.result())

    # using loop comprehension to run the loop
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something_with_arg, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # using map() the simplest way to run multithreading. the only disadvantage is that all the threads are kicked
    # in parallely but ended at once only and in order(one which starts first end first)
    executor.map(do_something_with_arg, secs)



finish = time.perf_counter()  # finishing counter
print(f'Total time taken is: {round(finish - start, 2)} seconds')
