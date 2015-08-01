class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def __len__(self):
        return len(self.vals)
        
    def findIntersect(self, other, c):
        if len(other) < 1:
            return self.c
        elif other[0] in self.vals:
            return self.findIntersect(other[1:], self.c.insert(other[0]))
        else:
            return self.findIntersect(other[1:], self.c)
        
    def intersect(self, other):
        self.c = intSet()
        return self.findIntersect( other.vals, self.c)
            
            
    
        
c1 = intSet()
c2 = intSet()
                
c1.insert(3)
c1.insert(1)
c1.insert(7)
c1.insert(9)
c1.insert(2)


c2.insert(4)
c2.insert(9)
c2.insert(3)
c2.insert(0)
c2.insert(1)
c2.insert(7)


print 
print c1
print c2


print len(c2)
c3 = c1.intersect(c2)
print c3
        