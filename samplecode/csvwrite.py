"""Write a simple CSV file
MCS 260 Fall 2020 Lecture 30 example"""

import csv
import fact  # to get the factorial function fact()

f = open("factorials.csv","w",encoding="UTF-8",newline="")
csvfile = csv.writer(f)

csvfile.writerow(["number","factorial"])
for n in range(10):
    L = [n,fact.fact(n)]
    csvfile.writerow(L)

f.close()
