"""Regular expression demonstrations
MCS 260 Fall 2020 Lecture 28
"""

import re
import sys

def demo1():
    """Minimal example of a regex"""
    s = "Avocado is usually considered a vegetable."
    print(re.sub("vegetable","fruit",s))

def demo2():
    """dot and repetition controls"""
    s = "Do not feed beans to bears"
    print(re.sub(r"b.{3}s","?",s))

def demo3():
    """start and end with s"""
    s = "Do not feed beans to bears or snakes"
    print(re.sub(r"s.+s","?",s))

def demo4():
    """low, low prices"""
    s = "A latte costs $18 and a Python textbook costs $599"
    print(re.sub(r"\$\d+","$0.99",s))

def demo5():
    """determines whether a string contains digits"""
    m = re.search(r"\d+",sys.argv[1])
    if m == None:
        print("No digits in {}".format(sys.argv[1]))
    else:
        print("Found this string of digits: {} (at positions {} to {})".format(
            m.group(),
            m.start(),
            m.end()
        ))

def demo6():
    """Find all contiguous groups of digits in sys.argv[1]"""
    L = re.findall(r"\d+",sys.argv[1])
    if L:
        for s in L:
            print("Found number:",s)
    else:
        print("No digits in",sys.argv[1])

def demo7():
    """Find all contiguous groups of digits in sys.argv[1]"""
    for m in re.finditer(r"\d+",sys.argv[1]):
        print("Found number {} at positions {} to {}".format(
            m.group(),
            m.start(),
            m.end()
        ))


if __name__=="__main__":
    demo7()