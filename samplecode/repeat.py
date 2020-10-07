"""Repeat a string a given number of times.
The first argument is the number of times.
The second gives the string to repeat.

MCS 260 Fall 2020 Lecture 12 - David Dumas
"""

import sys

if len(sys.argv) < 3:
    print("Usage:",sys.argv[0],"N s")
    print("Prints N copies of string s, one per line.")
else:
    n = int(sys.argv[1])
    s = sys.argv[2]
    for i in range(n):
        print(s)
