'''Project Euler 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
from math import factorial
def sumFactorialOfDigits():
    sum = 0
    #optimize to start at 145
    for i in range(145,9999999):
        if isSumOfFactorials(i):
            print i
            sum += i
    return sum 


def isSumOfFactorials(n):
    digits = str(n)
    sum = 0
    for i in digits:
        sum += factorial(int(i))
    
    return (sum == n)
print sumFactorialOfDigits()