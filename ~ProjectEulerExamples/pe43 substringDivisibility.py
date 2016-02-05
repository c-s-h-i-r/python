'''Project Euler 43 Sub String Divisibility
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
from Helpers import *
class pe43:

    def checkSubStringDivisibility(self,strOrNum):
        s = str(strOrNum)
        if int(s[1:4]) % 2 != 0:
            #not divisible by 2
            return False
        if int(s[2:5]) % 3 != 0:
            #not divisible by 3
            return False            
        if int(s[3:6]) % 5 != 0:
            #not divisible by 5
            return False
        if int(s[4:7]) % 7 != 0:
            #not divisible by 7
            return False
        if int(s[5:8]) % 11 != 0:
            #not divisible by 11
            return False
        if int(s[6:9]) % 13 != 0:
            #not divisible by 13
            return False
        if int(s[7:10]) % 17 != 0:
            #not divisible by 17
            return False
        return True
	
    def main(self):
        # get all 0-9 pandigital numbers
        sum = 0
        #takes long time
        pans = [''.join(p) for p in set(permutations('0123456789', 10))]
    #    for i in pans:
    #        print i
        for v in pans:
            if self.checkSubStringDivisibility(v):
                sum += int(v)
        print sum
            
if __name__ == "__main__":
    c = pe43()
    #print generatePandigital(5)
    c.main()