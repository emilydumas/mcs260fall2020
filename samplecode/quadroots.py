# Determine the number of real roots of a quadratic polynomial
# MCS 260 Fall 2020 Lecture 6 - David Dumas
print("Enter the coefficients a,b,c of ax^2+bx+c, in that order, one per line.")
a = float(input())
b = float(input())
c = float(input())

print("You entered:",a,"x^2 +",b,"x +",c)

discriminant = b**2 - 4*a*c

if discriminant > 0:
    print("This polynomial has two real roots.")
elif discriminant == 0:
    print("This polynomial has exactly one real root.")
else:
    # Now we know discriminant < 0
    print("This polynomial doesn't have any real roots.")
