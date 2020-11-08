"""Demo of file writing function for pytest lecture"""

def write_hello(fn):
    """Write the string 'hello world' to a new file
    with filename `fn`
    """
    f = open(fn,"w",encoding="UTF-8")
    f.write("hello world\n")
    f.close()

