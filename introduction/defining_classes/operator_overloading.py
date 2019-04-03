
"""
Euclid’s Algorithm
"""
def greatest_common_denominator(m,n):
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

    # def show(self):
    # This function will not work with print function, since it doesn't return a string.
    #     print(self.num, "/",self.den)       

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
                 # invoke helper function
        common = greatest_common_denominator(new_num , new_den)

        return Fraction(new_num// common, new_den  // common)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __sub__(self, otherfraction):

        new_num = self.num*otherfraction.den - self.den*otherfraction.num
        new_den = self.den*otherfraction.den
                 # invoke helper function for greatest common denominator
        common = greatest_common_denominator(new_num , new_den)

        return Fraction(new_num// common, new_den  // common)


    def __mul__(self, otherf):

        newnum = self.den * otherf.num
        newden = self.num * otherf.den

        common = greatest_common_denominator(newnum,newden)

        return Fraction(newnum// common, newden  // common)
    
    def __truediv__(self,otherfunc):

        new_numer = self.num * otherfunc.den
        new_denom = self.den * otherfunc.num

        common = greatest_common_denominator(new_numer,new_denom)

        return Fraction(new_numer// common, new_denom  // common)

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

    def __lt__(self, other):
        """
        The __lt__ method
        compares two objects and returns the Lesser of the 2 values
        """
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num < second_num

    def __gt__(self, other):
        """
        The __gt__ method
        compares two objects and returns the Greater of the 2 values
        """
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num > second_num

# One is to define a method called show that will allow the 
# Fraction object to print itself as a string. 
# this does not work in general. In order to make printing work properly, 
# we need to tell the Fraction class how to convert itself into a string.
# myf = Fraction(3,5)
# my.show()

def main():
    f = Fraction(1,3)
    g = Fraction(1,5)
    h = f+g
    print (f.getNum())
    print (g.getDen())
    j = Fraction(2,6)
    print('addition: ')
    print (h)
    print('subtraction: ')
    print (f - j)
    print('multiplication: ')
    print (f * j)
    print('division: ')
    print (f / j)
    print ('greater than: ')
    print ( g > f)
    print('less than: ')
    print ( g < f)
    print ('equality: ')
    print (g == f)
    print (f==j)
    print (f!=j)

main()