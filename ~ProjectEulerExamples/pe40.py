'''Project Euler 40
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 * d10  *d100  *d1000 * d10000 * d100000 *d1000000
'''

def makeSeries(limit):
    strnum = ""
    for i in range(1,limit):
        strnum += str(i)
    return strnum

def findValue(str):
    product = int(str[1-1]) * \
                int(str[10-1]) * \
                int(str[100-1]) * \
                int(str[1000-1]) * \
                int(str[10000-1]) *\
                int(str[100000-1]) * \
                int(str[1000000-1]) 
    return product
  
print findValue(makeSeries(1000000))