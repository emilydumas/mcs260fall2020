"""
Example of a worker thread that wakes up in response
to an Event object being set.
MCS 260 Fall 2020 Lecture 42 - David Dumas
"""

import threading
import time

# The integer that the worker thread
# is to operate on
workdata = 0

# Event to indicate a recalculation
# is needed
workdata_updated = threading.Event()

def worker_run():
    """Main function of the worker thread"""
    while True:
        # Wait for a signal that recalculation is needed
        workdata_updated.wait()
        # Acknowledge the signal so it doesn't trigger
        # another recalculation (after this one)
        workdata_updated.clear()
        x = workdata
        print("worker: Starting work on square of {}".format(x))
        time.sleep(2)
        print("worker: Calculated {}**2 = {}".format(x,x*x))

worker = threading.Thread(target=worker_run,daemon=True)
worker.start()

for i in range(20):
    time.sleep(0.5)
    workdata = i
    print("main: Updated workdata to {}, signaling worker thread to compute.".format(workdata))
    workdata_updated.set()
