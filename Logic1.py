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
    def squirrel_play(temp, is_summer):
        """
        temp -- integer
        is_summer -- boolean
        Returns True if the squirrels play and False otherwise.
        """
        if(temp > 59):
            if(temp < 91 or (is_summer and temp < 101)):
                return True
        return False
    @staticmethod
    def caught_speeding(speed, is_birthday):
        """
        speed -- integer > 0
        is_birthday -- boolean
        Returns int 0-no ticket, 1=small ticket, 2=big ticket.
        """
        if(is_birthday):
            speed -= 5
        if(speed > 60):
            if(speed > 80):
                return 2
            return 1
        return 0
    @staticmethod
    def sorta_sum(a, b):
        """
        a, b -- integers
        Returns the sum of a and b, except sums of [10,19] return 20.
        """
        sum = a + b
        return sum if(sum < 10 or sum > 19) else 20
    @staticmethod
    def alarm_clock(day, vacation):
        """
        day -- integer representing day of the week (0=Sum..6=Sat)
        vacation -- boolean
        Return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00", on weekend - "10:00"; vacation weekday - "10:00", weekend - "off"
        """
        if(day == 0 or day == 6):
            #weekend
            alarm = "10:00" if(not vacation) else "off"
    
        else:
            alarm = "7:00" if(not vacation) else "10:00"
        return alarm    
    @staticmethod
    def love6(a, b):
        """
        a, b -- integer
        Return True if either one is 6 or if their sum or difference is 6.
        """
        if(a != 6 and b != 6):
            if(a + b != 6):
                if(abs(a-b) != 6):
                    return False
                    
        return True
        
    @staticmethod
    def in1to10(n, outside_mode):
        """
        n -- integer
        outside_mode -- boolean
        """
        result = False
        if(1 <= n <= 10):
            result = True
        if(outside_mode and n != 1 and n!= 10):
            result = not result
        return result
        
    @staticmethod
    def near_ten(num):
        """
        num -- positive integer
        Returns True if num is within 2 of a multiple of 10.
        """
        remainder = num % 10 # 8,9,1,2,0
        if(remainder in [0,1,2,8,9]):
            return True
        return False
        
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
                    




    


