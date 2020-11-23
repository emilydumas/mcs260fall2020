"""
Basic threading example
MCS 260 Fall 2020 Lecture 39
"""

import threading
import time

def go():
    """Main function of the worker thread"""
    for i in range(10):
        time.sleep(1.2)
        print("Worker thread completed task",i)
    print("Worker thread DONE")

worker = threading.Thread(target=go)
worker.start()

for i in range(10):
    time.sleep(1)
    print("Main thread completed task",i)
print("Main thread DONE")

print("Waiting for worker...")
worker.join()
print("The worker seems to have finished.")