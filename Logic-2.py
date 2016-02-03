import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#List-1 methods codingbat
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
        return 0
        
    @staticmethod
    def make_bricks(small, big, goal):
        #small-1, big=5
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
        
        
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    