"""MCS 260 Lecture 19
Sample mini-shell
"""

import os

while True:
    s = input("-->")
    fields = s.split()
    cmd = fields[0]   # first word is the command name
    args = fields[1:] # all subsequent words are arguments to the command
    # So command "change sub"
    # would have cmd =="change"
    # and        args == ["sub"]
    if cmd == "exit":
        break
    elif cmd == "gps":
        # print current directory
        print(os.getcwd())
    elif cmd == "change":
        # change current directory

        # TODO: Move argument count checking and
        # error reporting into a separate function
        # so we don't duplicate code in each elif
        if len(args) != 1:
            print("ERROR: The change command requires one argument.")
            continue
        os.chdir(args[0])
    elif cmd == "vision":
        # list the files in the current directory
        # (the "visible" ones)
        for fn in os.listdir():
            print(fn)
    elif cmd[-1]=="?":
        fn = cmd[:-1]
        # check if the file cmd[:-1] exists
        if os.path.exists(fn):
            msg = "Yes, {} exists".format(fn)
            if os.path.isdir(fn):
                msg = msg + " and is a directory"
            elif os.path.isfile(fn):
                msg = msg + " and is a file"
            print(msg)
        else:
            print("No, {} does not exist".format(fn))
    else:
        print("ERROR: Unknown command: {}".format(cmd))