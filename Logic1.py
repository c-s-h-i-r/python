import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#List-1 methods codingbat
class Logic1:
    @staticmethod
    def cigar_party(cigars, is_weekend):
        """
        cigars -- integer
        is_weekend -- boolean
        Returns true if the party with the given values is successful.
        """
        if(cigars > 39):
            if(not is_weekend and cigars < 61 or is_weekend):
                return True
        return False
    @staticmethod
    def dat_fashion(you, date):
        """
        you -- integer [0..10]
        date -- integer [0..10]
        Return 0=no,1=maybe,2=yes
        """
        if(you < 3 or date < 3):
            return 0
        if(you > 7 or date > 7):
            return 2
        return 1
    @staticmethod
    def 
    
# Here's our unit tests.
class LogicTests(unittest.TestCase):
    obj = Logic1()

    def test1(self):
        self.assertEqual(self.obj.cigar_party(30, False), False)
        self.assertEqual(self.obj.cigar_party(50, True), True)
        self.assertEqual(self.obj.cigar_party(30, True), False)
        
   
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


