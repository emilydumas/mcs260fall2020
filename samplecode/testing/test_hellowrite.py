"""Demonstrate use of tmpdir in pytest"""

import hellowrite
import os

def test_write_hello(tmpdir):
    """Write to a file in a temporary directory"""
    fn = os.path.join(str(tmpdir),"out.txt")
    hellowrite.write_hello(fn)
    print("I just wrote to the file:",fn)

