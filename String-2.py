import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#List-1 methods codingbat
class String2:
    
# Here's our unit tests.
class StringTests(unittest.TestCase):
    obj = String2()
        
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


