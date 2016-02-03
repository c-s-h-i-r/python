import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#List-1 methods codingbat
class String2:
    def double_char(str):
        res = ''
        for x in str:
            res = res + x + x
        return res
  
    def count_hi(str):
        count = 0
  
        for x in xrange(0, len(str)-1):
            if str[x] == 'h':
                if len(str) > x and str[x+1] == 'i':
                    count += 1
        return count
        def cat_dog(str):
  
    countcat = 0
    countdog = 0
    for x in xrange(0, len(str)-1):
            if len(str) > x+3 and str[x:x+3] == 'cat':
                countcat += 1
            if len(str) > x+3 and str[x:x+3] == 'dog':
                countdog += 1
    return countcat == countdog
# Here's our unit tests.
class StringTests(unittest.TestCase):
    obj = String2()
        
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


