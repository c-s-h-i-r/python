'''module for helpers '''

def getTriangleNumbers(limit):
    '''return list of triangle numbers'''
    l = []
    for i in range(1,limit):
        num = (i * (i+1) )/2
        l.append(num)
    return l
    
def getPentagonalNumbers(limit):
    '''return list of pentagonal numbers'''
    l = []
    for i in range(1,limit):
        num = (i * (3*i-1) )/2
        l.append(num)
    return l
    
def getHexagonalNumbers(limit):
    '''return list of Hexagonal numbers'''
    l = []
    for i in range(1,limit):
        num = i * (2*i-1)
        l.append(num)
    return l


def getPrimes(limit):
    '''Get all primes up to limit'''
    arr = [True]*limit
    
    def sieve(x):
        for i in xrange(x*2, limit,x): 
            arr[i] = False
    map(sieve, xrange(2, limit**1/2))
    primes = [i for i in xrange(2, limit) if arr[i]]
    return primes

def isPrime(n):
    '''Check if n is prime.'''
    if n < 1:
        return False
    for i in xrange(int(n**1/2), 2, -1):
        if n % i == 0:
            return False
    return True


def generatePandigital(length = 9):
    '''# get all 0-length pandigital numbers
    '''
    digits = ''
    for i in range(length+1):
        digits += str(i)
    l = [''.join(p) for p in permutations(digits, len(digits))]
    return set(l)
    
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

    
def isPandigital(x, num = 9):
    #Check if an n digit number is num-digit pandigital
    d = str(x)
    comparArr = [0]*num
    
    for i in d:
        if int(i) != 0:
            if int(i) > (len(d)):
                return False
            comparArr[int(i)-1] = 1
    for i in comparArr:
        if i != 1:
            return False
    return True

def sumDigits(n):
    '''Return the sum of the digits of n'''
    num = str(n)
    sum = 0
    for i in num:
        sum += int(i)
    return sum
   
def fibonacciGreaterThan(limit):
    '''Return first fibonacci number greater than limit'''
    f1=34
    f2 = 55
    f0 = f1+f2
    index = 11
    while True:
        f0 = f1+f2
        if f0 > digitLength:
            return index-1
        f2 = f1
        f1 = f0
        f1 = f0
        index += 1
    return f0

def printMatrix(matrix):
    '''prints a list of lists'''
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))
    print "-------------------------"
    
    
def isSumOfFactorials(n):
    '''returns true if number is equal to the sum of its digits factorial.'''
    digits = str(n)
    sum = 0
    for i in digits:
        sum += factorial(int(i))
    
    return (sum == n)
    
def genrot(str):
    '''Generate a rotation of one for the number !as a string'''
    orig = str[:]
    while 1:
        str = str[-1:] + str[:-1]
        if str == orig: break
        yield str
        
def decToBin(n):
    '''return integer in binary string format'''
    return "{0:b}".format(n)

def isPalindrome(str):
    '''checks if string is palindrome.'''
    l = len(str)
    for i in range(0, (len(str)/2+1)):
        fc = str[i:i+1]
        lc = str[l-i-1:l-i]
        if fc != lc:
            return False
    return True