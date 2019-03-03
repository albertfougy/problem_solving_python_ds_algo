
"""
Euclid’s Algorithm
"""
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    """
    The first method that all classes should provide is the constructor.
    The constructor defines the way in which data objects are created.
    """
    def __init__(self , top, bottom):
        """
        self is a special parameter that will always be used as a reference back to the
        object itself. It must always be the first formal parameter; however, it will
        never be given an actual parameter value upon invocation.
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        """
         One of these, __str__, is the method to convert an object into a string. The
         default implementation for this method is to return the instance address string
         as we have already seen.
        """
        return str(self.num)+"/"+str(self.den)

    def __add__(self, other_fraction):

        new_num = self.num*other_fraction.den+self.den*other_fraction.num
        new_den = self.den*other_fraction.den
        common = gcd(new_num , new_den)

        return Fraction(new_num// common, new_den  // common)

    def __eq__(self, other):
        """
        We can create deep equality –equality by the same value,
        not the same reference–by overriding the __eq__ method. The __eq__ method
        is another standard method available in any class. The __eq__ method
        compares two objects and returns True if their values are the same, False otherwise.
        """
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)