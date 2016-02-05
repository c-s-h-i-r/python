'''Project Euler 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def sumDigits(n):
	num = str(n)
	sum = 0
	for i in num:
		sum += int(i)
	return sum
n = 2**1000
print n
print sumDigits(n)