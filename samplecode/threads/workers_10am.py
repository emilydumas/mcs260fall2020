"""
Worker threads in Python
MCS 260 Fall 2020 Lecture 39 (10am)
"""

# NOTE: This version of the program will run forever because
# the worker threads run out of jobs, but don't stop. See
# workers_10am_fixed.py for a version that fixes this.
# (But this version is the one developed in lecture.)

import threading
import time
import queue

def worker(name,Q):
    """Main function for each worker thread"""
    while True:
        job = Q.get()
        print("Worker {} received job {}".format(name,job))
        time.sleep(1)

job_queue = queue.Queue()

print("Starting worker threads")
workers = [ threading.Thread(target=worker, args=(i,job_queue)) for i in range(2) ]
for w in workers:
    w.start()

N = 0
for i in range(10):
    time.sleep(2)
    print("Adding a batch of 3 jobs to the queue")
    for j in range(3):
        job_queue.put(N)
        N += 1

print("The main thread is done.")
