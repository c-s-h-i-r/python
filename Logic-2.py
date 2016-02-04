import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#Logic-2 methods codingbat
class Logic2:
    @staticmethod
    def lone_sum(a, b, c):
        """
        a,b,c -- integers
        Return their sum; 
        If one of the values is a duplicate do not count it.
        """
        #set is unordered values - commonly used to remove duplicates 
        #from list

        orig = [a,b,c]
        #create list of duplicates from input
        dups = set([x for x in orig if orig.count(x) > 1])
        #return sum of duplicate set - original set
        return sum(list(set(orig)-dups))
               
    @staticmethod
    def lucky_sum(a,b,c):
        """
        a,b,c -- integers
        Return their sum.
        If a value is 13 then don't count it or the value to the right.
        """
        numbersToSum = [a,b,c]
        sum = 0
        for x in numbersToSum:
            if x == 13:
                break
            else:
                sum += x
        return sum
        
    @staticmethod
    def make_bricks(small, big, goal):
        #small-1, big=5 can we make goal with small and big?
        smallbigs = 0
        if small > 5:
            smallbigs = small / 5
            small = small % 5
                        
        if goal > 0:
            if goal >= 5:
                if goal/5 <= big + smallbigs:
                    #we have enough bigs+smalls
                    leftover = goal % 5
                    bigsneeded = goal/5
                    if bigsneeded <= big:
                        #we have enough bigs
                        if leftover <= small + smallbigs:
                            return True
                        else:
                            return False
                    else:
                        #we need some smalls+big
                        smallsneeded = (bigsneeded - big) * 5 + leftover
                        if smallsneeded > small + (smallbigs*5):
                            
                            return False
                        else:
                            return True
                        
                else:
                    return False
            if goal < 5:
                if small + (smallbigs*5) >= goal:
                    return True
                else:
                    return False
    
    @staticmethod
    def no_teen_sum(a, b, c):
        '''
        Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
        '''
        l = map(Logic2.fix_teen, [a,b,c])
        return sum(l)
    
    @staticmethod
    def fix_teen(n):
        ''' takes an int value and returns that value fixed for the teen rule.
        '''
        if not ( 20 > n > 12) or n in (15,16):
            return n
        return 0
        
    @staticmethod
    def round_sum(a,b,c):
        '''
        Given 3 ints, a b c, return the sum of their rounded values. 
        '''
        return sum(map(Logic2.round10, [a,b,c]))

    @staticmethod
    def round10(num):
        '''
        round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
        '''
        return int(round(num, -1))
               
    @staticmethod
    def close_far(a,b,c):
        '''Given three ints,a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
        '''
        if (abs(a-b) < 2 and abs(a-c) > 1 and abs(b-c) > 1) or ( abs(a-c) < 2 and abs(a-b) > 1 and abs(b-c) > 1):
            return True
        return False
        
    @staticmethod
    def make_chocolate(small, big, goal):
        '''We want to make a package of goal kilos of chocolate. 
        We have small bars (1 kilo each) and big bars (5 kilos 
        each). Return the number of small bars to use, assuming 
        we always use big bars before small bars. 
        Return -1 if it can't be done. 
        '''
        
        if big *5 > goal:
            smallNeeded = goal % 5
        else:
            smallNeeded = goal - (big*5)
        
        if small - smallNeeded  >= 0:
            return smallNeeded
        return -1
            
        
# Unit tests.
class LogicTests(unittest.TestCase):
    obj = Logic2()
    
    def testLoneSum(self):
        self.assertEqual(self.obj.lone_sum(1,2,3), 6)
        self.assertEqual(self.obj.lone_sum(3,2,3), 2)
        self.assertEqual(self.obj.lone_sum(3,3,3), 0)
    def test1(self):
        self.assertEqual(self.obj.lucky_sum(1,2,3),6)
        self.assertEqual(self.obj.lucky_sum(1,2,13),3)
        self.assertEqual(self.obj.lucky_sum(1,13,3),1)
    def test2(self):
        self.assertEqual(self.obj.make_bricks(4,1,4),True)
        self.assertEqual(self.obj.make_bricks(3,1,9),False)
        self.assertEqual(self.obj.make_bricks(3,2,10),True)
        self.assertEqual(self.obj.make_bricks(7,1,8),True)
        self.assertEqual(self.obj.make_bricks(3,2,10),True)
        self.assertEqual(self.obj.make_bricks(7,1,13),False)
    def test_no_teen_sum(self):
        self.assertEqual(self.obj.no_teen_sum(1, 2, 3), 6)
        self.assertEqual(self.obj.no_teen_sum(2, 13, 1), 3)
        self.assertEqual(self.obj.no_teen_sum(2, 1, 14), 3)
    def test_round_sum(self):
        self.assertEqual(self.obj.round_sum(16, 17, 18), 60)
        self.assertEqual(self.obj.round_sum(12, 13, 14), 30)
        self.assertEqual(self.obj.round_sum(6, 4, 4), 10)
    def test_close_far(self):
        self.assertEqual(self.obj.close_far(1, 2, 10), True)
        self.assertEqual(self.obj.close_far(1, 2, 3), False)
        self.assertEqual(self.obj.close_far(4, 1, 3), True)
    def test_make_chocolate(self):
        self.assertEqual(self.obj.make_chocolate(4, 1, 9), 4)
        self.assertEqual(self.obj.make_chocolate(4, 1, 10), -1)
        self.assertEqual(self.obj.make_chocolate(4, 1, 7), 2)
        
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    