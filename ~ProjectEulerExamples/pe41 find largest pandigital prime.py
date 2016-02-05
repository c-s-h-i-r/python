'''Project Euler 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
class myClass():
    def __init__(self):
        self._limit = 7654321
        self._arr = [True] * self._limit
   
    def getPrimes(self):
        map(self.sieve, xrange(2, self._limit**1/2))
        primes = [i for i in xrange(2, self._limit) if self._arr[i]]
        return primes

    def sieve(self, x):
        for i in xrange(x*2,self._limit,x): 
            self._arr[i] = False

   
    def isPandigital(self,x):
        #Check if an n digit number is n-digit pandigital
        d = str(x)
        comparArr = [0]*len(d)
        
        for i in d:
            if int(i) != 0:
                if int(i) > (len(d)):
                    return False
                comparArr[int(i)-1] = 1
        for i in comparArr:
            if i != 1:
                return False
        return True

    def main(self):
        #print self.isPandigital(123)
        import time
        a0 = time.clock()
        primes = self.getPrimes()
        a1 = time.clock()
        print "time for primes: ", a1-a0
        
        for i in primes:
            if(self.isPandigital(i)):
                print i
        
    
        
if __name__ == "__main__":
    c = myClass()
    c.main()
    

