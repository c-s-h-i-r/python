'''
Reciprocal Cycles
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

'''uses similar to long division by hand, count how many times we /10, it never actually calculates the number
'''
class ReciprocalCycles:
    def test(self):
        sequenceLength = 0
        position = 0
        for i in xrange(999,7,-1):
            if (sequenceLength >= i):
                break
            foundRemainders = [0] * i
            value = 1
            position = 0
         
            while (foundRemainders[value] == 0 and value != 0):
                foundRemainders[value] = position
                value *= 10
                value %= i
                position += 1
                 
            if (position - foundRemainders[value] > sequenceLength):
                sequenceLength = position - foundRemainders[value]    
        return sequenceLength, position
        
rc = ReciprocalCycles()

print rc.test()
