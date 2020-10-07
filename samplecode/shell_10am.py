"""A simple shell
MCS 260 Lecture 19 example
"""

import os

def bad_arg_count(cmd,args,n):
    """Print an error message if the length of
    args is not n, and return True."""
    if len(args)!=n:
        print("ERROR: {} requires {} argument(s)".format(cmd,n))
        return True
    return False

while True:
    s = input("$>")
    s = s.strip() # remove leading and trailing spaces
    fields = s.split()  # break into space separated components
    cmd = fields[0]   # command name (e.g. "movedir")
    args = fields[1:] # command arguments (e.g. "..")
    # TODO: Unify argument count logic into a single check.
    if cmd == "exit":
        break
    elif cmd == "whereami":
        if bad_arg_count(cmd,args,0):
            continue
        print(os.getcwd())
    elif cmd == "movedir":
        if bad_arg_count(cmd,args,1):
            continue
        os.chdir(args[0])
    elif cmd == "listf":
        if bad_arg_count(cmd,args,0):
            continue
        for fn in os.listdir():  # iterate over files in CWD
            print(fn)
    elif cmd == "makedir":
        if bad_arg_count(cmd,args,1):
            continue
        try:
            os.mkdir(args[0])
        except OSError as e:
            print("ERROR: {}".format(e))
    else:
        print("ERROR: Unknown command {}".format(cmd))



