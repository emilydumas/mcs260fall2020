"""Lazy finite geometric sequences"""

class FiniteGeometricSequence:
    """Finite geometric sequence that computes
    terms only as needed (is "lazy")
    """
    def __init__(self,start,ratio,length):
        """Initialize geometric sequence with first term
        `start`, ratio of successive terms `ratio` and
        total number of terms `length`.
        """
        self.start = start
        self.ratio = ratio
        self.length = length

    def __getitem__(self,idx):
        """Compute a term in the geometric sequence"""
        # TODO: Decide whether negative indices should
        # be an error (as now) or if they should count
        # from the end of the sequence (as with lists)
        if idx < 0 or idx >= self.length:
            raise IndexError("index {} not valid for geometric sequence of length {}".format(
                idx,
                self.length  
            ))
        
        return self.start * self.ratio**idx
        # Reminder: PEMDAS means this evaluates as
        # self.start * (self.ratio**idx)

    def __str__(self):
        """Human-readable string representation"""
        return "{}(start={},ratio={},length={})".format(
            self.__class__.__name__,
            self.start,
            self.ratio,
            self.length
        )

    def __setitem__(self,idx,val):
        """Modify either the start or ratio using
        item assignment
        """
        if idx==0:
            # change start
            self.start = val
        else:
            # change the ratio so that
            # the term at index idx becomes
            # val
            self.ratio = (val/self.start)**(1/idx)

    def __repr__(self):
        """Unambiguous string representation"""
        return str(self)

    def __len__(self):
        """Number of terms in the sequence"""
        return self.length