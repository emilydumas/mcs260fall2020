"""
Illustrate how to have two threads safely accessing
a single object using a Lock.

MCS 260 Fall 2020 Lecture 42 - David Dumas
"""

import threading
import time
import random

# dict mapping some integers to their names
names = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

# Shared global dict containing the current
# integer and its name
numdata = {
    "int": 5,
    "name": names[5]
}
numdata_lock = threading.Lock()

def worker_run():
    """
    Main function of worker thread which just
    prints the current integer and name on a
    regular basis.
    """
    while True:
        print("worker: waiting for numdata_lock")
        numdata_lock.acquire()
        print("worker: acquired numdata_lock")
        print("The number {} is spelled '{}'".format(numdata["int"],numdata["name"]))
        numdata_lock.release()
        time.sleep(1)

# Run worker_run() in a daemon thread
w = threading.Thread(target=worker_run,daemon=True)
w.start()

# Change the integer randomly 10 times
for i in range(10):
    time.sleep(3)
    # Choose a random key from the dict names
    x = random.choice(list(names.keys()))

    # BEGIN update of numdata
    numdata_lock.acquire()
    numdata["int"] = x
    # Uncomment the next line to make it MORE likely
    # the other thread wakes up during update
    time.sleep(1)
    numdata["name"] = names[x]
    numdata_lock.release()
    # END update of numdata
