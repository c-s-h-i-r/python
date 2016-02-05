''' Project Euler 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by 
cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from fractions import Fraction, gcd


def trythis():
    '''print the denominator of the product of the four fractions that follow this unusual pattern'''
    #given fraction ab/cd, if they have a digit in common, and we remove the digit is it the same fraction
    list = []
    for j in range(1,10):
        for k in range(1,10):
            for i in range(1,10):
                 #skip last digit ==0
                if i % 10 == 0 and j % 10 == 0 or j >= k:
                    continue

                # xa/xd;    
                beforeNum = int(str(i) + str(j))
                beforeDen = int(str(i) + str(k))
                beforeSimpleFrac = Fraction(beforeNum,beforeDen)
                afterSimpleFrac = Fraction(j,k)
                if(Fraction(j,k)== beforeSimpleFrac):
                    list.append(beforeSimpleFrac)
                
                #xa/dx; 
                beforeNum = int(str(i) + str(j))
                beforeDen = int(str(k) + str(i))
                beforeSimpleFrac = Fraction(beforeNum,beforeDen)
                afterSimpleFrac = Fraction(j,k)
                if(Fraction(j,k) == beforeSimpleFrac):
                    list.append(beforeSimpleFrac)
                
                #ax/dx; 
                beforeNum = int(str(j) + str(i))
                beforeDen = int(str(k) + str(i))
                beforeSimpleFrac = Fraction(beforeNum,beforeDen)
                afterSimpleFrac = Fraction(j,k)
                if(Fraction(j,k) == beforeSimpleFrac):
                    list.append(beforeSimpleFrac)
                    
                #ax/xd; 
                beforeNum = int(str(j) + str(i))
                beforeDen = int(str(i) + str(k))
                beforeSimpleFrac = Fraction(beforeNum,beforeDen)
                afterSimpleFrac = Fraction(j,k)
                if(Fraction(j,k) == beforeSimpleFrac):
                    list.append(beforeSimpleFrac)
    
    #If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    product = Fraction(1,1)
    for f in list:
        product *= f
    print product.denominator
    
    
trythis()
