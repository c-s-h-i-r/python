import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#warmup 1 methods codingbat
class Warmup1:

    '''
    def __init__(self):
        #constructor method for class
        self.data = ''
    '''    
    @staticmethod
    def sleep_in(weekday, vacation):
        '''weekday - boolean; vacation - boolean
        The parameter weekday is True if it is a weekday, and the
        parameter vacation is True if we are on vacation. We sleep
        in if it is not a weekday or we're on vacation.

        Return True if we sleep in.
        '''
        sleepIn = True if (weekday == False) or (vacation == True) else False
        return sleepIn

    @staticmethod
    def monkey_trouble(a_smile, b_smile):
        '''We have two monkeys, a and b, and the parameters a_smile and b_smile
        indicate if each is smiling. We are in trouble if they are both smiling or
        if neither of them is smiling.

        Return True if we are in trouble.
        '''
        return (True if (a_smile == b_smile) else False)

    @staticmethod
    def sum_double(a, b):
        '''Given two int values, return their sum.
        Unless the two values are the same,
        then return double their sum.
    '''
        sum = (a+b) if (a != b) else (2*(a+b))
        return sum

    @staticmethod
    def diff21(n):
        '''Given an int n, return the absolute difference between n and 21,
        except return double the absolute difference if n is over 21
        '''
        diff = abs(n-21)
        diff = 2*diff if n > 21 else diff
        return diff

    @staticmethod
    def parrot_trouble(talking, hour):
        '''We have a loud talking parrot.
    The "hour" parameter is the current hour time in the range 0..23.
    We are in trouble if the parrot is talking and the hour is before 7 or after 20.
    Return True if we are in trouble.
    '''
        return (True if (talking and (hour < 7 or hour > 20)) else False)


    @staticmethod
    def makes10(a, b):
        '''Given 2 ints, a and b,
        return True if one of them is 10 or their sum is 10
    '''
        return True if ((a+b) == 10) or (a == 10 or b == 10) else False

    @staticmethod
    def near_hundred(n):
      '''Given an int n
        Return true if it is within 10 of 100 or 200 '''
      diff = abs(100 - n)
      diff2 = abs(200-n)
      return True if (diff <= 10 or diff2 <= 10) else False

    @staticmethod
    def pos_neg(a, b, negative):
        """Given 2 int values, return True if one os negative and one is positive.
        Except if the parameter "negative" is True, then return True only if both
        are negative
    """
        isNeg = True if (a*b < 0) else False
        if (negative):
            isNeg = True if(a < 0 and b < 0) else False

        return isNeg

    @staticmethod
    def not_string(str):
        """Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    """
        
        if (str[0:3] != "not"):
            str = 'not ' + str

        return str
    @staticmethod
    def missing_char(str, n):
        """Given a non-empty string and an int n, return a new string where the
    char at index n has been removed. The value of n will be a valid index of a
    char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
    """
        if(len(str) < 1 or n > len(str) + 1):
            raise MyError("invalid arguements")

        newstring = str[:n] + str[n+1:]
        return newstring

    @staticmethod
    def front_back(str):
        """Given a string, return a new string where the first and last chars have
    been exchanged.
    """
        n = len(str)
        if(n < 2):
            return str
        newstring = str[-1:] + str[1:-1] + str[:1]
        return newstring

    
        

    
# Here's our "unit tests".
class WarmupTests(unittest.TestCase):
    obj = Warmup1()
    
    def test1(self):
        self.assertEqual(self.obj.sleep_in(False, False), True)
        self.assertEqual(self.obj.sleep_in(True, False), False)
        self.assertEqual(self.obj.sleep_in(False, True), True)

    ###
    #tests for monkey_trouble method
    def test2(self):
        self.assertEqual(self.obj.monkey_trouble(True,True) ,True)
        self.assertEqual(self.obj.monkey_trouble(False, False) , True)
        self.assertEqual(self.obj.monkey_trouble(True, False) , False)
    ###
    #tests for sum_double method
    def test3(self):
        self.assertEqual(self.obj.sum_double(1,2) , 3)
        self.assertEqual(self.obj.sum_double(3,2) ,5)
        self.assertEqual(self.obj.sum_double(2,2) , 8)
    ###
    #tests for diff21 method
    def test4(self):
        self.assertEqual(self.obj.diff21(19) , 2)
        self.assertEqual(self.obj.diff21(10) , 11)
        self.assertEqual(self.obj.diff21(21) , 0)
    ###
    #tests for parrot_trouble method
    def test5(self):
        self.assertEqual(self.obj.parrot_trouble(True, 6), True)
        self.assertEqual(self.obj.parrot_trouble(True, 7) , False)
        self.assertEqual(self.obj.parrot_trouble(False, 6) , False)
    ###
    #tests for makes10 method
    def test6(self):
        self.assertEqual(self.obj.makes10(9,10),True)
        self.assertEqual(self.obj.makes10(9,9) , False)
        self.assertEqual(self.obj.makes10(1,9) , True)
    ###
    #tests for near_hundred method
    def test7(self):
        self.assertEqual(self.obj.near_hundred(93) , True)
        self.assertEqual(self.obj.near_hundred(90) ,True)
        self.assertEqual(self.obj.near_hundred(111) , False)
    #tests for pos_neg method
    def test8(self):
        self.assertEqual(self.obj.pos_neg(1, -1, False) , True)
        self.assertEqual(self.obj.pos_neg(-1, 1, False) , True)
        self.assertEqual(self.obj.pos_neg(-4, -5, True) , True)
    #tests for not_string method
    def test9(self):
        self.assertEqual(self.obj.not_string('candy') , 'not candy')
        self.assertEqual(self.obj.not_string('x') , 'not x')
        self.assertEqual(self.obj.not_string('not bad') , 'not bad')
    #tests for missing_char method
    def test10(self):
        self.assertEqual(self.obj.missing_char('kitten', 1) , 'ktten')
        self.assertEqual(self.obj.missing_char('kitten', 0) , 'itten')
        self.assertEqual(self.obj.missing_char('kitten', 4) , 'kittn')
#tests for front_back
    def test11(self):
        self.assertEqual(self.obj.front_back('code') , 'eodc')
        self.assertEqual(self.obj.front_back('a') , 'a')
        self.assertEqual(self.obj.front_back('ab') , 'ba')


def main():
    unittest.main()
    #input("Press Enter to close") # Python 3 keeps cmd window open

if __name__ == '__main__':
    main()
                    




    


