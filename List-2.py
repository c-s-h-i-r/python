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
    
    @staticmethod
    def sum13(nums):
        '''Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
        '''
        if len(nums) < 1:
            return 0
        sum = 0
        nums_iter = iter(nums)
        for i in nums_iter:
            if i == 13:
                next(nums_iter, None)
                next(nums_iter)
            else:
                sum += i
        return sum
    
    def sum13_withoutiter(nums):
        '''Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
        '''
        count = 0
        while count < len(nums):
            if nums[count] == 13:
                del nums[count:count+2]
                continue
            count += 1
        return sum(nums)

    @staticmethod
    def sum67(nums):
        '''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
        '''
        # mark = False
        # for ind, num in enumerate(nums):
            # if num == 6:
                # mark = True
            # if mark:
                # nums[ind] = 0
            # if num == 7:
                # mark = False
        # return sum(nums)
        exists6 = True
        while exists6:
            try:
                indexOf6 = nums.index(6)
                indexOf7 = nums.index(7,indexOf6)
                del nums[indexOf6:indexOf7+1]
            except:
                exists6 = False
        return sum(nums)
    
    @staticmethod
    def has22(nums):
        '''
            Given an array of ints, return True if the 
            array contains a 2 next to a 2 somehwere.
        '''
        return (2,2) in zip(nums, nums[1:])
        
        
# Here's our unit tests.
class ListTests(unittest.TestCase):
    obj = List2()
    
    def test1(self):
        self.assertEqual(self.obj.centered_average([1,2,3,4,100]), 3)
    def test2(self):
        self.assertEqual(self.obj.count_hi('abc hi ho'), 1)
    def test_sum13(self):
        self.assertEqual(self.obj.sum13([1,2,2,1]), 6)
    def test_sum67(self):
        self.assertEqual(self.obj.sum67([1, 2, 2]),5)
        self.assertEqual(self.obj.sum67([1, 2, 2, 6, 99, 99, 7]), 5)
        self.assertEqual(self.obj.sum67([1, 1, 6, 7, 2]),4)
        self.assertEqual(self.obj.sum67([1, 6, 1, 7, 1, 6, 7, 2]), 4)
    def test_has22(self):
        self.assertEqual(self.obj.has22([1, 2, 2]) , True)
        self.assertEqual(self.obj.has22([1, 2, 1, 2]) , False)
        self.assertEqual(self.obj.has22([2, 1, 2]) , False)
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


