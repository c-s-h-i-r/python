'''Project Euler 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def getPrimes():
    limit = 999984
    arr = [True] * limit
    def sieve(x):
	global arr,limit
	for i in xrange(x*2,limit,x): arr[i] = False
    map(sieve, xrange(2,limit**1/2))
    primes = [i for i in xrange(2,limit) if arr[i]]

with open('primes.txt', 'r') as f:
    line = f.read()
primeList = line.split(', ')

def isprime(x):
	global primes
	# Longer, more thorough test: is it in the primes array?
	try:
		primes.index(x)
		return True
	except:
		return False
def isInPrime(x):
    st = str(x)
    return (st in primeList)
    
def isTruncatable(n, left=True):
    num = str(n)
    if left:    
        for i in range(len(num)):
 #           print i
  #          print "isTruncatable %s" %num[i:]
            if not isInPrime(num[i:]):
                return False
    else:
        for i in range(1,len(num)):
#            print "isTruncatable %s" %num[:-i]
            if not isInPrime(num[:-i]):
                return False

    return True
def isBothTruncable(n):
    #right now it checks n twice
    return isTruncatable(n) and isTruncatable(n, False)

def findSum():
    sum = 0
    for i in primeList:
        if isBothTruncable(i):
            sum += int(i)
    return sum - 2-3-5-7
print getPrimes()
