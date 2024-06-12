# powers of 2
# MCS 260 Fall 2020, Tue Sep 1 discussion meeting
# Jennifer Vaccaro

# Notes [added by Emily Dumas]:
# (1) This script illustrates several ways to compute powers of 2 in Python
# (2) This is "preview" code: It illustrates some recent material, but it also
# uses some Python features that we haven't discussed yet.  It was presented
# at the Sep 1 discussion meeting both to illustrate past material and to
# offer a preview of things to come.


def pow2_0(pow):
    return 2**pow

def pow2_1(pow):
    return 1<<pow

def pow2_2(pow):
    n=1
    for i in range(pow):
        n = n*2
    return n

def pow2_3(pow):
    n=1
    for i in range(pow):
        n=n+n
    return n  

def pow2_4(pow):
    if (pow==0):
        return 1
    else:
        return 2*pow2_4(pow-1)    

if __name__ == '__main__':
    print("n = 5")
    print("pow2_0(5) = ",pow2_0(5))
    print("pow2_1(5) = ",pow2_1(5))
    print("pow2_2(5) = ",pow2_2(5))
    print("pow2_3(5) = ",pow2_3(5))
    print("pow2_4(5) = ",pow2_4(5))
