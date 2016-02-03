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
        ''''''
        count = 0
  
        for x in xrange(0, len(str)-1):
            if str[x] == 'h':
                if len(str) > x and str[x+1] == 'i':
                    count += 1
        return count
    
    def cat_dog(str):
        ''''''
        catCount = 0
        dogCount = 0

        for i in range(len(str)-1):
            if str[i:i+3] == 'cat':
                catCount += 1
            if str[i:i+3] == 'dog':
                dogCount += 1
        return dogCount == catCount

    def count_code(str):
        count = 0
        for i in range(len(str)-1):
            if str[i:i+2] == 'co':
                if str[i+3:i+4] == 'e':
                    count += 1  
        return count
        
# Here's our unit tests.
class StringTests(unittest.TestCase):
    obj = String2()
        
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


