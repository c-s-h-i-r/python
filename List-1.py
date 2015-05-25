import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#List-1 methods codingbat
class List1:
    @staticmethod
    def first_last6(nums):
        """
        nums --array of ints
        Return true if 6 appears as either the first or last element of the array.
        """
        if(len(nums) < 1):
            return False
        return True if(nums[0] == 6 or nums[len(nums)-1] == 6) else False
    @staticmethod
    def same_first_last(nums):
        """
        nums -- array of ints
        Return True if the array if length 1 or more, and first and last element are equal.
        """
        n = len(nums)
        if(n > 0):
            if(nums[0] == nums[n-1]):
                return True
        return False
    @staticmethod
    def make_pi():
        """ return first 3 elements of PI in a list format. """
        return [3,1,4]
    @staticmethod
    def common_end(a, b):
        """
        a, b -- array of ints
        Returns True if they have the same first element or the same last element.
        """
        lenA = len(a)
        lenB = len(b)
        if(lenA > 0 and lenB > 0):
            if(a[0] == b[0] or a[lenA-1] == b[lenB-1]):
                return True
        return False
    @staticmethod
    def sumarr(nums):
        """
        nums -- array of ints
        return the sum of all elements in an array.
        """
        sum = 0
        for x in nums:
            sum += x
        return sum
    @staticmethod
    def rotate_left(nums):
        """
        nums -- array of ints
        Returns an array with the elements left shifted once.
        """
        newList = nums[1:] + [nums[0]]
        return newList
    @staticmethod
    def reverse(nums):
        """
        nums -- array of ints
        Returns a reversed array.
        """
        return nums[::-1]
    @staticmethod
    def max_end(nums):
        """
        nums -- array of ints
        Replace all elements of the array with max(first element, last element).
        """
        n = len(nums)
        if(n < 1):
            return []
        maximum = max(nums[0], nums[n-1])
        return [maximum] * n
        
# Here's our unit tests.
class ListTests(unittest.TestCase):
    obj = List1()
    
    def test1(self):
        self.assertEqual(self.obj.first_last6([1,2,6]), True)
        self.assertEqual(self.obj.first_last6([6]), True)
        self.assertEqual(self.obj.first_last6([1,2,6,8]), False)
    def test2(self):
        self.assertEqual(self.obj.same_first_last([1, 2, 3]) , False)
        self.assertEqual(self.obj.same_first_last([1, 2, 3, 1]) , True)
        self.assertEqual(self.obj.same_first_last([1, 2, 1]) , True)
    def test3(self):
        self.assertEqual(self.obj.make_pi(), [3,1,4])
    def test4(self):
        self.assertEqual(self.obj.common_end([1,2,3],[7,3]), True)
        self.assertEqual(self.obj.common_end([1,2,3],[7,3,2]), False)
        self.assertEqual(self.obj.common_end([1,2,3],[1,3]), True)
    def test5(self):
        self.assertEqual(self.obj.sumarr([1,2,3]), 6)
        self.assertEqual(self.obj.sumarr([]), 0)
        self.assertEqual(self.obj.sumarr([7,0,0,0]), 7)
    def test6(self):
        self.assertEqual(self.obj.rotate_left([1,2,3]), [2,3,1])
        self.assertEqual(self.obj.rotate_left([5,11,9,435]), [11,9,435,5])
        self.assertEqual(self.obj.rotate_left([1]), [1])
    def test7(self):
        self.assertEqual(self.obj.reverse([]), [])
        self.assertEqual(self.obj.reverse([1,2,3]), [3,2,1])
        self.assertEqual(self.obj.reverse([0,3,4,0,23]), [23,0,4,3,0])
    def test8(self):
        self.assertEqual(self.obj.max_end([]), [])
        self.assertEqual(self.obj.max_end([1,2,3]), [3,3,3])
        self.assertEqual(self.obj.max_end([1,2,3,4,2,1]), [1,1,1,1,1,1])
#    def test9(self):
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#    def test10(self):
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#    def test11(self):
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#    def test12(self):
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


