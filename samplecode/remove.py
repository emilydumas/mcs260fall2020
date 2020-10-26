"""Remove a file or directory (including all contents)
MCS 260 Fall 2020 Lecture 27 example
"""

import sys
import os

def remove(fn):
    """Remove fn if it is a file.  Remove contents of fn
    and then fn it is a directory.
    """
    if os.path.isfile(fn):
        # files can be removed directly
        print("Removing file: ",fn)
        os.remove(fn)
    elif os.path.isdir(fn):
        # directory: must remove all files first
        print("Removing contents of dir: ",fn)
        for subfn in os.listdir(fn):
            # Recursive call to remove each item
            # in the directory
            remove(os.path.join(fn,subfn))
        print("Removing the dir: ",fn)
        os.rmdir(fn)
    else:
        # encountered something that isn't a file or dir
        raise Exception("Encountered '{}' which is not a regular file or directory".format(fn))

def main():
    """Remove sys.argv[1]"""
    if len(sys.argv) == 1:
        print("Usage: {} FILE_OR_DIR_TO_REMOVE".format(sys.argv[0]))
        sys.exit()
    fn = sys.argv[1]
    s=input("About to remove '{}'; proceed? (y/n)".format(fn))
    if s == 'y':
        # -------------------------------------------------------
        # Disable the program so no one accidentally deletes all
        # of their files while trying it out.
        print("This example code is dangerous. It will permanently remove")
        print("a directory and all of it contents.  If you really want to")
        print("do this, remove this message and the sys.exit() call after")
        print("it from the source code.")
        sys.exit()
        # -------------------------------------------------------
        remove(sys.argv[1])

if __name__=="__main__":
    main()