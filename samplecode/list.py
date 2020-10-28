"""Recursively list the contents of a directory
MCS 260 Fall 2020 example
"""

import os
import sys

def list_files(fn,indent=""):
    """
    If fn is a file, print its name.
    If fn is a directory, print its name and then
    print its contents.
    """
    if os.path.isfile(fn):
        # Handle a regular file

        # Right now `fn` contains a full path, possibly
        # including a bunch of directory names. We'd 
        # like to strip away everything except the last
        # component, so instead of printing
        #     vegetables\greens\cooking\kale
        # we'd like to print
        #     kale
        # The function os.path.basename does this.
        print(indent + os.path.basename(fn))
    elif os.path.isdir(fn):
        # Handle a directory

        # First print its name with a slash after it
        # (os.sep is either '\' or '/')
        print(indent+os.path.basename(fn) + os.sep)
        for sub in os.listdir(fn):
            # Call list_files recursively to deal with
            # this item in the directory.
            list_files(os.path.join(fn,sub),indent+"    ")
    else:
        raise Exception("Encountered '{}' which is not a regular file or directory.".format(fn))

def main():
    """List contents of sys.argv[1] recursively"""
    if len(sys.argv)<2:
        print("Usage: {} DIRNAME".format(sys.argv[0]))
        sys.exit()
    fn = sys.argv[1]
    list_files(fn)
    
if __name__=="__main__":
    main()