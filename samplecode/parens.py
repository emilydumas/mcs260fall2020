"""Check arithmetic expression for balanced parentheses"""
# MCS 260 Fall 2020 Lecture 14 - David Dumas

print("Enter an arithmetic expression in parentheses:")
s = input().strip()

paren_stack = []
for i,c in enumerate(s):
    if c == "(":
        paren_stack.append(i)
    elif c == ")":
        if len(paren_stack) == 0:
            # Too many right parentheses
            print("ERROR: Extra right parenthesis")
            print(s)
            print(i*" " + "^")
            break
        paren_stack.pop()

if len(paren_stack) > 0:
    # Unclosed left parenthesis
    i = paren_stack.pop()  # Where was the left paren that's open?
    print("ERROR: Unclosed parenthesis")
    print(s)
    print(i*" " + "^")


