'''Project Euler 36
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def decToBin(n):
    '''return integer in binary string format'''
    return "{0:b}".format(n)
    

def isPalindrome(str):
    l = len(str)
    for i in range(0, (len(str)/2+1)):
        fc = str[i:i+1]
        lc = str[l-i-1:l-i]
        if fc != lc:
            return False
    return True
            
def findAll():
    sum = 0
    for i in range(1,1000000):
    
        if(i % 2 != 0 and isPalindrome(str(i)) and isPalindrome(decToBin(i))):
            sum += i
    return sum
    
print findAll()
