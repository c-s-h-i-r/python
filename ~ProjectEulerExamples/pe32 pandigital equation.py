'''Project Euler 32
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

#stop after deciding if it can be written as pandigital

def isPandigital(multiplicand, multiplier, product):
    digits = []
    digits.append(str(multiplicand))
    digits.append(str(multiplier))
    digits.append(str(product))
    d = ''.join(digits)
    ten = [0]*9
    if(len(d) != 9):
        return False
        
    for i in d:
        if int(i) != 0:
            ten[int(i)-1] = 1
#    print ten
    for i in ten:
        if i != 1:
            return False
#    print multiplicand, multiplier, product
    return True

def canBeWritten(n):
    
    for i in range(1, int(n**1/2)):
        if n % i == 0:
            #found divisor
            if isPandigital(n/i, i, n):
                return True
    return False
            
def sumOfPandigitalProducts():
    #get all sums of products that can be written as a 1-9 pandigital
    sum = 0
    for i in range(9999):
        #revise upper bound
        if(canBeWritten(i)):
            sum += i
    return sum
        
#print isPandigital(406,13,5278)
print sumOfPandigitalProducts()
    