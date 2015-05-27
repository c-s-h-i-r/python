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
    @staticmethod
    def sum2(nums):
        """
        nums -- array of ints
        Returns the sum of the first two elements of the array. [Or whatever is there]
        """
        sum = 0
        for index, x in enumerate(nums):
            if(index > 1):
                break
            sum += x
        return sum
    @staticmethod
    def middle_way(a, b):
        """
        a, b -- integer arrays
        Returns a new array of length 2 containing their middle elements.
        Raises MyError is a list is empty.
        """
        lenA = len(a)
        lenB = len(b)
        if(lenA < 1 or lenB < 1):
            raise MyError("Error: lists cannot be empty.")
        return [a[(lenA-1)//2], b[(lenB-1)//2]]
    @staticmethod
    def make_ends(nums):
        """
        nums -- integer array
        Returns a new array length 2 containing the first and last elements in the nums array.
        """
        n = len(nums)

        if(n < 2):
            newArray = nums * 2
        else:
            newArray = [nums[0], nums[n-1]]
        return newArray
    @staticmethod
    def has23(nums):
        """
        nums -- integer array
        Returns True if contains 2 or 3.
        """
        for x in nums:
            if(x == 2 or x == 3):
                return True
        return False
    
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
    def test9(self):
        self.assertEqual(self.obj.sum2([1,2,3]), 3)
        self.assertEqual(self.obj.sum2([]), 0)
        self.assertEqual(self.obj.sum2([-1, 34, 0, 2]), 33)
    def test10(self):
        self.assertEqual(self.obj.middle_way([1,2,3],[4,5,6]), [2,5])
        self.assertEqual(self.obj.middle_way([0,1],[4,4,5,3]), [0,4])
        self.assertRaises(MyError, lambda: self.obj.middle_way([], [0,123,123,234,4]))
    def test11(self):
        self.assertEqual(self.obj.make_ends([1,2,3]), [1,3])
        self.assertEqual(self.obj.make_ends([]), [])
        self.assertEqual(self.obj.make_ends([1,1,1,1,4,5]),[1,5])
    def test12(self):
        self.assertEqual(self.obj.has23([2,5]), True)
        self.assertEqual(self.obj.has23([4,3]), True)
        self.assertEqual(self.obj.has23([2.5, 0]), False)
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


