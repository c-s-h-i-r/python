'''Goldbach's other conjecture  Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import Helpers

class pe46:
    
    def __init__(self):
        self._triNums = []
        
    def genCompositeNums(self):
        '''generates composite numbers (has at least 1 positive factor other than itself and one.'''
        for i in xrange(1,100000):
            if(not Helpers.isPrime(i)):
                yield i
         
    
    def main(self):
        
    
if __name__ == "__main__":
    c = pe46()
    c.main()