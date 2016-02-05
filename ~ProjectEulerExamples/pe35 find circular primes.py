''' Project Euler 35
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
# rotation generator
def genrot(str):
	orig = str[:]
	while 1:
		str = str[-1:] + str[:-1]
		if str == orig: break
		yield str
	
# Generate primes up to 1,000,000
print 'Sieving...'
limit = 1000000
arr = [True] * limit
def sieve(x):
	global arr,limit
	for i in xrange(x*2,limit,x): arr[i] = False
map(sieve, xrange(2,limit**1/2))
primes = [i for i in xrange(2,limit) if arr[i]]

# Slow test for primeness
def isprime(x):
	global primes
	# Quick test - any even or '5' digits?
	for c in str(x):
		if ['1','3','7','9'].count(c) == 0: return False;
	# Longer, more thorough test: is it in the primes array?
	try:
		primes.index(x)
		return True
	except:
		return False

def isCirc(x):
	for y in genrot(str(x)):
		if not isprime(int(y)):
			return False
	return True

# Test for circularness
print 'Circulizing...'
circs = [x for x in primes if isCirc(x)]
print len(circs)