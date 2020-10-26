"""Example of recursion: factorial
MCS 260 Fall 2020 Lecture 27 example
"""

import sys

def fact(n):
    """Factorial of a nonnegative integer n"""
    if n<=1:
        return 1
    return n*fact(n-1)

def main():
    """Test fact()"""
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
    else:
        x = 18
    print("fact({}) = {}".format(x,fact(x)))

if __name__=="__main__":
    main()
