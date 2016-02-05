# -*- coding: utf-8 -*-
'''
Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
import Helpers
class DistinctPrimesFactors():
    def __init__(self):
        # Generate primes up to 1,000,000
        print 'Sieving...'
        limit = 1000000
        arr = [True] * limit
        def sieve(x):
            for i in xrange(x*2,limit,x): arr[i] = False
        map(sieve, xrange(2,limit**1/2))
        self.primes = [i for i in xrange(2,limit) if arr[i]]
        print 'Sieved.'
        self.main()
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
    
    def getPrimeFactors(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return list(set(factors))
                
    def main(self):

        for i in xrange(, 16):
            primes1 = self.getPrimeFactors(i-2)
            primes2 = self.getPrimeFactors(i-1)
            primes2 = self.getPrimeFactors(i)
            if len(primes1) == 3 and len(primes2) == 3 and cmp(primes1, primes2) != 0 and cmp(primes1, primes3) != 0 and cmp(primes2, primes3) != 0:
                #check length and values
                #make this to be totally distinct
                print i-1, i
        
        
DistinctPrimesFactors()