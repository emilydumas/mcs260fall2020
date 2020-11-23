"""
Worker threads in Python (fixed version)
MCS 260 Fall 2020 Lecture 39 (10am)
"""

# NOTE: This is an improved version of the example developed
# in Lecture 39.  The worker threads in this one look for
# a value of "None" in the queue, and if they receive it, 
# they stop.  The main program thus has a way to signal 
# that the workers should stop, allowing the program to
# end.

import threading
import time
import queue

def worker(name,Q):
    """Main function for each worker thread"""
    while True:
        job = Q.get()
        # Is this job a signal that the worker should exit?
        if job == None:
            print("Exit signal received by worker {}".format(name))
            return
        # If we get here, it is a regular job
        print("Worker {} received job {}".format(name,job))
        time.sleep(1)

job_queue = queue.Queue()

print("Starting worker threads")
workers = [ threading.Thread(target=worker, args=(i,job_queue)) for i in range(2) ]
for w in workers:
    w.start()

N = 0
for i in range(5):
    time.sleep(2)
    print("Adding a batch of 5 jobs to the queue")
    for j in range(5):
        job_queue.put(N)
        N += 1

print("Done adding work.  Submitting exit signals to the queue.")

for i in range(2):
    job_queue.put(None)

print("Main thread exiting.  The workers should exit when they're done.")
