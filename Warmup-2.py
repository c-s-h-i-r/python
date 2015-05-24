import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#warmup 2 methods codingbat
class Warmup2:

    @staticmethod
    def string_times(str, n):
        """Given a string and a non-negative int n,
    return a larger string that is n copies of the original string.
    """
        return str*n
    @staticmethod
    def front_times(str, n):
        """Given a string and a non-negative int n,
we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3.
Return n copies of the front; 
"""
        if(len(str) < 3):
            newstring = str
        else:
            newstring = str[:3]
        newstring *= n
        return newstring
    @staticmethod
    def string_bits(str):
        """Given a string, return a new string made of every other char starting with the first
    """
        return str[::2]
    @staticmethod
    def string_splosion(str):
        """Given a non-empty string like "Code"
        return a string like CCoCodCode.
        """
        newstring = ""
        for i in range(1, len(str)+1):
            newstring = newstring + str[0:i]
        return newstring
    @staticmethod
    def last2(str):
        """Given a string, return the count of the number of times that the last 2 characters appear
        in the string as a substring
        """
        if(len(str) < 2):
            return 0
        last2 = str[-2:]
        count = 0
        for i in range(0, len(str)-2):
            substr = str[i:i+2]
            count += 1 if substr == last2 else 0
        return count
    
    @staticmethod
    def array_count9(nums):
        """
        nums -- array of ints
        Returns the number of 9's in the array
        """
        count = 0
        for i in nums:
            count += 1 if (i==9) else 0

        return count
    @staticmethod
    def array_front9(nums):
        """
         nums -- array of ints
         Returns True if one of the first 4 elements is 9.
         """
        if(len(nums) < 1):
            return False
        for i in nums[0:3]:
            if(i == 9):
                return True
        return False
    @staticmethod
    def array123(nums):
        """
        nums -- array of ints
        Returns True if subset appears in the array somewhere
        """
        subset = [1,2,3]
        if(len(nums) < 3):
            return False
        for i in range(0,len(nums)-2):
            if(subset == nums[i:i+3]):
                 return True
        return False
    @staticmethod
    def string_match(a, b):
        """
        a, b -- strings
        Returns the number of positions where they contain the same length 2
        substring.
        """
        count = 0
        minLength = len(a) if(len(a) < len(b)) else len(b)
        for i in range(minLength-1):
            if( a[i:i+2] == b[i:i+2]):
                count += 1
        return count

    
def cmp(a, b):
    return (a > b) - (a < b)
    

        
# Here's our "unit tests".
class WarmupTests(unittest.TestCase):
    obj = Warmup2()
    
    def test1(self):
        self.assertEqual(self.obj.string_times('HiHo', 2), 'HiHoHiHo')
        self.assertEqual(self.obj.string_times("It's off to work we go", 1), "It's off to work we go")
        self.assertEqual(self.obj.string_times("", 2), "")
    def test2(self):
        self.assertEqual(self.obj.front_times("Chocolate", 2), "ChoCho")
        self.assertEqual(self.obj.front_times("az", 4), "azazazaz")
        self.assertEqual(self.obj.front_times("", 2), "")
    def test3(self):
        self.assertEqual(self.obj.string_bits('Hello'), 'Hlo')
        self.assertEqual(self.obj.string_bits('Hi') , 'H')
        self.assertEqual(self.obj.string_bits('Heeololeo') , 'Hello')
    def test4(self):
        self.assertEqual(self.obj.string_splosion('Code'), 'CCoCodCode')
        self.assertEqual(self.obj.string_splosion('abc'), 'aababc')
        self.assertEqual(self.obj.string_splosion('ab'), 'aab')
    def test5(self):
        self.assertEqual(self.obj.last2('hixxhi'), 1)
        self.assertEqual(self.obj.last2('xaxxaxaxx'), 1)
        self.assertEqual(self.obj.last2('axxxaaxx'), 2)
    def test6(self):
        self.assertEqual(self.obj.array_count9([1,2,9]), 1)
        self.assertEqual(self.obj.array_count9([1,9,9]), 2)
        self.assertEqual(self.obj.array_count9([1,9,9,3,9]), 3)
    def test7(self):
        self.assertEqual(self.obj.array_front9([1,2,9,3,4]), True)
        self.assertEqual(self.obj.array_front9([1,2,3,4,9]), False)
        self.assertEqual(self.obj.array_front9([1,2]), False)
    def test8(self):
        self.assertEqual(self.obj.array123([1, 1, 2, 3, 1]), True)
        self.assertEqual(self.obj.array123([1, 1, 2, 4, 1]), False)
        self.assertEqual(self.obj.array123([1, 1, 2, 1, 2, 3]), True)
    def test9(self):
        self.assertEqual(self.obj.string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(self.obj.string_match('abc','abc'), 2)
        self.assertEqual(self.obj.string_match('abc', 'axc'), 0)
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


