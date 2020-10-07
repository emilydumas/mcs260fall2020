"""Unary calculator from lecture 15
MCS 260 Fall 2020 - David Dumas"""

# This was developed as a live coding example
# You can (and should) watch the video of it being 
# written at:
# https://uic.zoom.us/rec/share/-9gW0yEvaBiGoWLHd1BKQOwDaDDlOKnYB1D53izwPvMn_NWRCz5nN8LtS9OiLut6.2h2PfeQgG0n7Gsdk

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
    else:
        cmd,argstr = s.split()
        arg = float(argstr)
        # cmd is the command, as a string
        # arg is the argument, as a float
        
        if cmd in commands:
            # e.g.
            # val = multiply(val,arg) if given "mul"
            # val = add(val,arg) if given "add"
            # val = subtract(val,arg) if given "sub"
            val = commands[cmd](val,arg)
        else:
            print("ERROR: Unrecognized command: {}".format(cmd))
