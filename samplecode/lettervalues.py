"""Compute the "value" of a word, if each letter is
worth a different number of points specified in a 
file.
MCS 260 Fall 2020 Lecture 13 - David Dumas
"""
# A sample data file vals.txt is available at
# https://dumas.io/teaching/2020/fall/mcs260/samplecode/vals.txt

import sys

if len(sys.argv) != 3:
    print("Usage:",sys.argv[0],"valuefile word")
    print("Read values for each alphabet letter from `valuefile`")
    print("in the format letter,value, e.g.:")
    print("a,1\nb,3\nc,3\nd,2")
    print("Then, compute the value of `word` and print it.")
    sys.exit()  # exits the program immediately

fin = open(sys.argv[1],"r")
vals = dict()
for line in fin:
    ltr,valstr = line.split(",")
    vals[ltr] = int(valstr)
fin.close()

score = 0
for c in sys.argv[2]:
    ltrval = vals[c.lower()]
    print(c,"has value",ltrval)
    score = score + ltrval

print("'{}' gets total score {}".format(sys.argv[2],score))
