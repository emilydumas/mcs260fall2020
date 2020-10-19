"""Classes for representing planar geometric objects"""

class Circle:
    """Circle in the plane"""
    def __init__(self,cx,cy,r):
        """Initialize circle from center (cx,cy) and radius r"""
        self.cx = float(cx)
        self.cy = float(cy)
        self.r = float(r)
    
    def __str__(self):
        """Human-readable representation of the object"""
        return "Circle(cx={},cy={},r={})".format(
            self.cx,
            self.cy,
            self.r
        )

    def __repr__(self):
        """Unambiguous string representation of the object"""
        return str(self)

    # R == S
    # -->
    # R.__eq__(S)
    # -->
    # Circle.__eq__(R,S)
    def __eq__(self,other):
        """Is this circle equal to other, in the sense
        of having the same center and radius?
        """
        if not isinstance(other,Circle):
            return False

        return self.cx == other.cx and self.cy == other.cy and self.r == other.r

    def translate(self,dx=0.0,dy=0.0):
        """Translate by vector (dx,dy)"""
        self.cx += dx
        self.cy += dy

    def scale(self,factor):
        """Apply a uniform scale about the center"""
        self.r *= factor

class Rectangle:
    """Axis-parallel rectangle in the plane"""
    def __init__(self,cx,cy,w,h):
        self.cx = float(cx)
        self.cy = float(cy)
        self.w = float(w)
        self.h = float(h)

    def __str__(self):
        """Human-readable representation of the object"""
        return "Rectangle(cx={},cy={},w={},h={})".format(
            self.cx,
            self.cy,
            self.w,
            self.h
        )

    def __eq__(self,other):
        """Is this rectangle equal to other, in the sense
        of having the same center, width, and height?
        """
        if not isinstance(other,Rectangle):
            return False

        return self.cx == other.cx and self.cy == other.cy and self.w == other.w and self.h == other.h

    def __repr__(self):
        """Unambiguous string representation of the object"""
        return str(self)

    def translate(self,dx=0.0,dy=0.0):
        """Translate by vector (dx,dy)"""
        self.cx += dx
        self.cy += dy

    def scale(self,factor):
        """Apply a uniform scale about the center"""
        self.w *= factor
        self.h *= factor
