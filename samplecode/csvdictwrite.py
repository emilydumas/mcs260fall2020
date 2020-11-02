"""Write a simple CSV file using DictWriter
MCS 260 Fall 2020 Lecture 30 example"""

import csv
import fact  # to get the factorial function fact()

f = open("factorials2.csv","w",encoding="UTF-8",newline="")
csvfile = csv.DictWriter(f,fieldnames=["number","factorial"])

csvfile.writeheader() # print the field names on a header row
for n in range(10):
    d = dict()
    d["number"] = n
    d["factorial"] = fact.fact(n)
    csvfile.writerow(d)

f.close()
