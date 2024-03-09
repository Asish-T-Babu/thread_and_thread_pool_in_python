import threading
import time

def worker(thread_number):
    time.sleep(2)
    print('Done',thread_number)

# Here every thread is executed at a time, we can't limit the number of threads to be used in the process and for each task assigned to thread will create a new thread and perform the operations then destroy the thread
# these below threads are independent, individual threads, not belong to a group, a category etc
t1 = threading.Thread(target=worker, args=('t1',))
t1.start()
t2 = threading.Thread(target=worker, args=('t2',))
t2.start()
t3 = threading.Thread(target=worker, args=('t3',))
t3.start()
t4 = threading.Thread(target=worker, args=('t4',))
t4.start()
t5 = threading.Thread(target=worker, args=('t5',))
t5.start()


# Threading
# is a technique that allows you to run multiple threads concurrently. This can be useful for tasks that can be broken down into smaller, independent tasks. For example, you could use threading to download multiple files at the same time or to process multiple images in parallel.
# Thread pool
# is a collection of threads that are pre-created and ready to be used. When you need to run a task, you can simply submit it to the thread pool, and one of the available threads will execute it. This can be more efficient than creating a new thread for each task, as it avoids the overhead of creating and destroying threads.
# summarizes the key differences between threading and thread pool:

# When to use
# Threading - When you need to run multiple independent tasks concurrently.
# Thread pool - When you need to run a large number of tasks concurrently, or when you need to avoid the overhead of creating and destroying threads.

# How it works
# Threading - Creates a new thread for each task.
# Thread pool - Uses a pre-created pool of threads to execute tasks.

# Efficiency
# Threading - Can be less efficient than thread pool, as it incurs the overhead of creating and destroying threads.
# Thread pool - Can be more efficient than threading, as it avoids the overhead of creating and destroying threads.


# Overall, thread pool is a more efficient way to run multiple tasks concurrently in Python. However, threading can be useful for tasks that can be broken down into smaller, independent tasks.

##############################################################################################################################################

# what is thread overhead

# Thread overhead is the cost of creating, executing, and destroying threads. Thread pools can help avoid the overhead of creating and destroying threads. Thread pools can:
# Improve performance
# Improve resource utilization
# Limit the number of concurrent threads
# Prevent overloading the system
# Reuse threads
# Help ensure that tasks are executed in a timely manner