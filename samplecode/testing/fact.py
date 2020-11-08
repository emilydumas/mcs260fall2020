"""Factorial as an example of recursion
MCS 260 Fall 2020 Lecture 27 example
"""

import sys

def fact(n):
    """Factorial of n, computed recursively"""
    if n <= 1:
        # Both 0! and 1! are equal to 1
        # return these values immediately
        return 1

    # Otherwise, use recursive formula.
    return n * fact(n-1)

def main():
    """Demonstrates fact() function"""
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
    else:
        x = 5
    print("fact({}) = {}".format(x,fact(x)))

if __name__=="__main__":
    main()