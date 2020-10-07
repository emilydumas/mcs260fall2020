"""Number the lines of a file specified on command line"""
import sys
fin = open(sys.argv[1],"r")
n = 0
for line in fin:
    n = n+1
    print(n,line,end="") # line usually has \n at the end
fin.close()
