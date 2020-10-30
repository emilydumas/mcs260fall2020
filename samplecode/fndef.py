"""Find function definitions
MCS 260 Fall 2020 Lecture 29 example"""

import sys
import re

# regex to match a Python function definition, i.e.
# "def", then whitespace, then a name, then parentheses and colon.
# Capture the name in a group.
# Extra whitespace is allowed everywhere except in the name.
# This is not perfect; we use these simplifications:
#  * We only look for names consisting of alphabet
#    letters and digits (but must not start with a digit!)
#  * We don't consider the possibility of multiple ")"
#    characters appearing on a single line
pat = r"\s*def\s+([A-Za-z_][0-9A-Za-z_]*)\s*\(.*\)\s*:"

# Open a text file specified on the command line
f = open(sys.argv[1],"r")

# Check each line for matching the pattern
for line in f:
    m = re.match(pat,line)
    if m:
        print("Found a function called: {}".format(m.group(1)))
