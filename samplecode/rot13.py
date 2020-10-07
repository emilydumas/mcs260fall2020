# Rot13 cipher simple implementation
# MCS 260 Fall 2020 Lecture 7 - David Dumas

# Note: Only lower-case letters supported!

clear  = "abcdefghijklmnopqrstuvwxyz "
cipher = "nopqrstuvwxyzabcdefghijklm "

intext = input("Message: ")
outtext = ""

for c in intext:
    for i,d in enumerate(clear):
        if c == d:
            outtext = outtext + cipher[i]
            break  # exits the inner for loop

print("Encoded:",outtext)
