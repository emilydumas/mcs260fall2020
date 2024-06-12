"""Simulate getting ready to go out in winter"""
# MCS 260 Fall 2020 Lecture 14 - Emily Dumas

print("Enter items worn, in order put on:")
L = []
while True:
    s = input().strip()
    if s == "":
        break
    L.append(s)

print("Ok. Press Enter when ready to remove winter gear.")
input()
while len(L)>0:
    s = L.pop()
    print("Remove",s,"and press Enter when ready.")
    input()


