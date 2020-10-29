"""Regular expression demo code"""

import re

def demo1():
    """Minimal re example"""
    s = "Avocado is usually considered a vegetable."
    print(re.sub("vegetable","fruit",s))

def demo2():
    """Single char replacement demo"""
    s = "Avocado is usually considered a vegetable."
    print(re.sub("o","0",s))

def demo3():
    """Replace prices in dollars with -PRICE-"""
    s = "A latte costs $18 and a new Python textbook costs $599"
    print(re.sub(r"\$\d+","-PRICE-",s))

def demo4():
    """Example of using match objects"""
    pat = r"h.{3}l"
    s = "apple hot s zucchini hovel python"
    m = re.search(pat,s)
    if m == None:
        print("The pattern '{}' was not found in string '{}'".format(
            pat,
            s
        ))
    else:
        # there was a match
        print("The pattern '{}' was found in string '{}'; the match was '{}' at character {} to {}".format(
            pat,
            s,
            m.group(),
            m.start(),
            m.end()
        ))

if __name__=="__main__":
    demo4()