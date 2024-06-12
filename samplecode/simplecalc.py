# Prefix calculator for one-digit operands
# MCS 260 Fall 2020 Lecture 7 - Emily Dumas

while True:
    s = input("> ")
    if s == "exit":
        break
    cmd = s[:3]    # 3 char command
    x = int(s[4])  # 1 digit operand
    y = int(s[6])  # 1 digit operand
    if cmd == "add":
        print(x+y)
    elif cmd == "sub":
        print(x-y)
    elif cmd == "mul":
        print(x*y)
    elif cmd == "div":
        print(x/y)
    elif cmd == "exp":
        print(x**y)
    else:
        print("ERROR: Unknown command",cmd)

        