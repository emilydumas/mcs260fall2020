"""
Functions to implement codes that rotate letter positions
in the latin alphabet
"""

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()

def rotate(s,steps=13):
    """
    Rotate latin alphabet letters from string `s` forward by
    `steps` positions.  Wrap around to start of alphabet if
    end is reached.  Return the result.
    """
    senc = ""
    for c in s:
        if c in uppercase:
            # Upper case letter: rotate
            i = uppercase.index(c)
            senc += uppercase[(i+steps)%len(uppercase)]
        elif c in lowercase:
            # Lower case letter: rotate
            i = lowercase.index(c)
            senc += lowercase[(i+steps)%len(lowercase)]
        else:
            # Other character: add to output unchanged
            senc += c

    return senc
