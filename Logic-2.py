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
        
    
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


