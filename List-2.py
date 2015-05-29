import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#List-1 methods codingbat
class List2:
    @staticmethod
    def count_evens(nums):
        evens = 0
        for x in nums:
            if(x % 2 == 0):
                evens += 1
        return evens
    @staticmethod
    def big_diff(nums):
        if(len(nums) > 1):
            low = min(nums[0], nums[1])
            high = max(nums[0], nums[1])
            for x in nums[1:]:
                if(x > high):
                    high = x
                else:
                    if(x < low):
                        low = x
            return high - low
        return 0
    @staticmethod
    def centered_average(nums):
  
        if(len(nums) > 2):
            average = 0
            low = nums[0]#not efficient
            high = nums[0]
            for x in nums:
                if(x > high):
                    high = x
                else:
                    if(x < low):
                        low = x
                average += x
            return (average - (high + low)) // (len(nums)-2)
        return 0
    @staticmethod
    def count_hi(str):
        count = 0
        for index in range(len(str)):
            if(str[index:index+2] == "hi"):
                count += 1
        return count
    
# Here's our unit tests.
class ListTests(unittest.TestCase):
    obj = List2()
    
    def test1(self):
        self.assertEqual(self.obj.centered_average([1,2,3,4,100]), 3)
    def test2(self):
        self.assertEqual(self.obj.count_hi('abc hi ho'), 1)
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


