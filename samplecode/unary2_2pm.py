"""Unary calculator REPL
Originally developed in Lecture 15
Updated with error handling in Lecture 17
MCS 260 (2pm) - David Dumas
"""

# This was developed as a live coding example
# The error handling was added in this video:
# https://uic.zoom.us/rec/share/kPEoCrGkFWvAsYwVYU7d4fTzpAJUFmekVXyuGoXAXORCma-qI1LmTyAIr7sp3Ia5.8zOP7cXdPwdUJ5SM
# The original version was developed in this video:
# TODO: ADD URL WHEN VIDEO IS DONE PROCESSING
# (These videos are only accessible to students in MCS 260 in Fall 2020)

def add(current, argument):
    """Add the argument to the current value"""
    return current+argument

def subtract(current, argument):
    """Subtract the argument from the current value"""
    return current-argument

def multiply(current, argument):
    """Multiply the argument and the current value"""
    return current*argument

def divide(current, argument):
    """Divide the current value by the argument"""
    return current/argument

def load(current, argument):
    """Return the argument"""
    return argument

# All known commands, mapping to the functions
# that handle them
commands = {
    "add": lambda c,a: c+a,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
    "load": load,
    "power": lambda c,a: c**a,
}

# This variable stores the float on the calculator
# display, and we initialize it to 0.0
val = 0.0

while True:
    # print the current value
    print("{:12.3f}".format(val))
    # read a command
    s = input(">")

    if s == "exit":
        break

    if s == "help":
        print("I know about these commands:")
        for c in commands:
            print(c)
        continue

    try:
        # split the line into a command and argument    
        cmd,argstr = s.split()
    except ValueError:
        print("ERROR: Malformed command: {}".format(s))
        continue

    try:
        # convert the argument to a float
        arg = float(argstr)
    except ValueError:
        print("ERROR: Not recognized as a number: {}".format(argstr))
        continue

    if cmd in commands:
        # Known command
        # If cmd is "add" and arg is 5
        # this will do  add(val,5)
        # If cmd is "mul" and arg is 5
        # this will do  multiply(val,5)
        try:
            val = commands[cmd](val,arg)
        except Exception as e:
            print("ERROR: Command failed: {}".format(e))
    else:
        print("ERROR: I don't know how to {}".format(cmd))
