"""Unary calculator
Originally developed in Lecture 15
Updated with error handling in Lecture 17
MCS 260 Fall 2020 - David Dumas"""

# This was developed as a live coding example
# The error handling was added in this video:
# https://uic.zoom.us/rec/share/cTMt2NTlhyzRgcJfsFpdIkh-OE-RzD3OHQ_wJFRW_lKspnshwNS3B2QEO5tGi3RD.zhqe6DXEmCF3q89d
# The original version was developed in this video:
# https://uic.zoom.us/rec/share/-9gW0yEvaBiGoWLHd1BKQOwDaDDlOKnYB1D53izwPvMn_NWRCz5nN8LtS9OiLut6.2h2PfeQgG0n7Gsdk
# (These videos are only accessible to students in MCS 260 in Fall 2020)

def add(current, argument):
    """Adds argument to current and returns the result"""
    return current+argument

def subtract(current, argument):
    """Subtracts argument from current and returns the result"""
    return current-argument

def multiply(current, argument):
    """Multiplies argument by current and returns the result"""
    return current*argument

def divide(current, argument):
    """Divides current by argument and returns the result"""
    return current/argument

def load(current, argument):
    """Returns argument"""
    return argument

# DATA about what commands are supported
commands = {
    "add": add,
    "mul": multiply,
    "sub": subtract,
    "div": divide,
    "power": lambda c,a: c**a,
    "load": load,   
}

val = 0.0

while True:
    print("{:12.3f}".format(val))
    s = input(">") # read the full command
    
    if s == "exit":
        break

    if s == "help":
        print("The following commands are known:")
        for c in commands:
            print(c)
        continue

    # if we make it here, then the command is not
    # help and is not exit.
    try:
        cmd,argstr = s.split()
    except ValueError:
        print("ERROR: Malformed command: {}".format(s))
        continue

    try:
        arg = float(argstr)
    except ValueError:
        print("ERROR: Invalid float: {}".format(argstr))
        continue
    
    # cmd is the command, as a string
    # arg is the argument, as a float
    
    if cmd in commands:
        # e.g.
        # val = multiply(val,arg) if given "mul"
        # val = add(val,arg) if given "add"
        # val = subtract(val,arg) if given "sub"
        try:
            val = commands[cmd](val,arg)
        except Exception as e:
            print("ERROR: Command failed: {}".format(e))
    else:
        print("ERROR: Unrecognized command: {}".format(cmd))
