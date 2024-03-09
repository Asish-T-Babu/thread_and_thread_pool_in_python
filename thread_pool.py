from concurrent.futures import ThreadPoolExecutor
import time

def worker(number):
    print(f'Calculating the result for number {number}')
    time.sleep(2)
    return number ** 2


pool = ThreadPoolExecutor(2) # Here we are limiting the number of thread been used by the thread pool, ThreadPoolExecutor is taking a integer parameter which is the count of thread to be used at a time
work1 = pool.submit(worker, 7)
work2 = pool.submit(worker, 9)
work3 = pool.submit(worker, 5)
work4 = pool.submit(worker, 5)
work5 = pool.submit(worker, 8)

print('Hello world') # this will be printed immediately after start the all work and it will not wait for any threads to be completed

time.sleep(5) # This line of code is for stop execution for 5 seconds so the thread 3(work3) complete its execution, so in line no 33 it will print the result

##############################################################################################################
# Here the below code will wait for the execution untill the work3 execute its task and return result

# print(work3.result())
# print('hello') # This hello will be printed after completing the work3 task and print the result 

#############################################################################################################

# we can check a thread is completed its execution or not using the below code
print("Work3 completed?",work3.done()) # if the task is been finished print then it will result True otherwise it will return False

# To prevent the waiting we can do like this 
if work3.done():
    print(work3.result())

#############################################################################################################
# Shutting down the pool

# we can assign to task to the pool using the pool.submit() function, if we shutdown the pool then no one can assign a new task after shutdown the Thread pool.(if we want any new task to assign to this pool then  we will shutdown the task, the above process before shutdown will work like normally(it will work like what it work before))
work6 = pool.submit(worker, 2) # This code will work and generate teh output

pool.shutdown()
work6 = pool.submit(worker, 2) # After shutdown we are trying to execute a new task, here it will through an error ('cannot schedule new futures after shutdown')