"""
Producer-consumer pattern example
MCS 260 Fall 2020 Lecture 39 (2pm)
"""

import threading
import time
import queue

def worker_main(name,Q):
    """Main function of the worker threads"""
    print("Worker {} starting".format(name))
    while True:
        # Retrieve work from the queue
        job = Q.get()
        if job == None:
            print("Worker {} got the exit indicator".format(name),flush=True)
            return
        time.sleep(1)
        print("Worker {} completed job {}".format(name,job),flush=True)

job_queue = queue.Queue()

workers = [ 
    threading.Thread(target=worker_main,args=(1,job_queue)),
    threading.Thread(target=worker_main,args=(2,job_queue))
]
for w in workers:
    w.start()

N = 0
for i in range(5):
    time.sleep(2)
    print("Main thread is adding 5 jobs to the queue")
    for j in range(5):
        job_queue.put(N)
        N += 1

print("Main thread is done. Adding two Nones to the queue.")
job_queue.put(None)
job_queue.put(None)
