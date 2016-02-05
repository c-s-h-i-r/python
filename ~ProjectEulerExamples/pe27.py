'''
Euler discovered the remarkable quadratic formula:
n*n + n + 41
It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
by 41, and certainly when n = 41, 41*41 + 41 + 41 is clearly divisible by 41.
The incredible formula 79n + 1601 was discovered, which produces 80 primes 
for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479

Considering quadratics of the form:
n*n + an + b, where |a| < 1000 and |b| < 1000
where n is the modulus/absolute value of n
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
def QuadraticPrimes():
#optimize!	
    #find inputs which produce the max number of primes
    max = 0; a = 0; b = 0
    for i in range(-1000,1000, 1):
        for j in range(-1000, 1000, 1):
            res = numPrimes(i, j)
            if(res > max):
                max = res
                a = i
                b = j
    return a*b

    
#count the primes for consecutive inputs
def numPrimes(a, b):
    count = 0
    i=0
    while True:
        result = i*i + a*i + b
        if isPrime(result):
            count += 1
        else:
            break
        i += 1
    return count

from  math import sqrt
def isPrime(n):
    if n < 1:
        return False
    for i in xrange(int(sqrt(n)), 2, -1):
        if n % i == 0:
            return False
    return True

result = QuadraticPrimes()
print "NumPrimes: ", result