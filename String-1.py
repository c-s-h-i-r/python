import unittest

#my simple exception class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#String-1 methods codingbat
class String1:

    @staticmethod
    def hello_name(name):
        """
        name -- string
        Returns a greeting of the form "Hello <name>!".
        """
        return "Hello " + name + "!"
    @staticmethod
    def make_abba(a, b):
        """
        a, b -- string
        Return the result of putting them together and then in the reverse order.
        """
        return (a + b + b + a)
    @staticmethod
    def make_tags(tag, word):
        """
        tag -- string; type of HTML tag
        word -- string to go in between HTML tags
        """
        return "<" + tag + ">" + word + "</" + tag + ">"
    @staticmethod
    def make_out_word(out, word):
        """
        out -- string, length == 4
        word -- string
        Return a new string with 'word in the middle of the out string.
        """
        middleIndex = len(out) // 2
        newstring = out[:middleIndex] + word + out[middleIndex:]
        return newstring
    @staticmethod
    def extra_end(str):
        """
        str -- string
        Returns a new string made of 3 copies of the last 2 chars of the original string.
        """
        n = len(str)
        if(n < 2):
            last2 = str
        else:
            last2 = str[-2:]
        return last2*3
    @staticmethod
    def first_two(str):
        """
        str -- string
        Returns the string made of its first two chars.
        """
        n = len(str)
        if(n < 2):
            first2 = str
        else:
            first2 = str[:2]
        return first2
    @staticmethod
    def first_half(str):
         """
         str -- string
         Returns the first half (floor(length/2)) of the string input.
         """
         half = str[:(len(str)//2)]
         return half
    @staticmethod
    def without_end(str):
        """
        str -- string with length at least 2
        Returns the input string without the first and last char.
        """
        n = len(str)
        if(n < 2):
            raise MyError("Error: Input string to short")
        return str[1:n-1]

    @staticmethod
    def combo_string(a, b):
        """
        a -- string
        b -- string
        Returns a string of the form short+long+short (meaning the size of the string inputs)
        Note: Strings must not be the same length! (Or else non-deterministic results)
        """
        lenA = len(a)
        lenB = len(b)
        if(lenA == lenB):
            raise MyError("Warning: input strings must not be the same length.")
        if(lenA < lenB):
            #a is shorter
            newstring = a + b + a
        else:
            newstring = b + a + b
        return newstring

    @staticmethod
    def non_start(a, b):
        """
        a,b -- strings
        Returns the strings concatenated, without the first char of each.
        """
        first = ''
        last = ''
        if(len(a) < 1):
            first = a
        else:
            first = a[1:]
        if(len(b) < 1):
            last = b
        else:
            last = b[1:]

        return first + last
    @staticmethod
    def left2(str):
        """
        str -- string
        Returns a 'rotated left 2' version where the first 2 chars are moved to the end of the string.
        """
        if(len(str) < 2):
            return str
        return str[2:] + str[:2]
        
        
# Here's our unit tests.
class StringTests(unittest.TestCase):
    obj = String1()
    
    def test1(self):
        self.assertEqual(self.obj.hello_name("chris"), "Hello chris!")
        self.assertEqual(self.obj.hello_name("Xuatu"), "Hello Xuatu!")
        self.assertEqual(self.obj.hello_name(""), "Hello !")
    def test2(self):
        self.assertEqual(self.obj.make_abba('Hi', 'Bye'), 'HiByeByeHi')
        self.assertEqual(self.obj.make_abba('Hi', 'Ho'), 'HiHoHoHi')
        self.assertEqual(self.obj.make_abba('bat', 'cat'), 'batcatcatbat')
    def test3(self):
        self.assertEqual(self.obj.make_tags('i','Yay'), "<i>Yay</i>")
        self.assertEqual(self.obj.make_tags('b','BOLD'), "<b>BOLD</b>")
        self.assertEqual(self.obj.make_tags('','Invalid syntax'), "<>Invalid syntax</>")
    def test4(self):
        self.assertEqual(self.obj.make_out_word('<<>>','word'), "<<word>>")
        self.assertEqual(self.obj.make_out_word('[[]]','arraycontent'), "[[arraycontent]]")
        self.assertEqual(self.obj.make_out_word('{[[{[{}]}]]}', 'aa'), "{[[{[{aa}]}]]}")
    def test5(self):
        self.assertEqual(self.obj.extra_end("Hello"), "lololo")
        self.assertEqual(self.obj.extra_end("ohhho"), "hohoho")
        self.assertEqual(self.obj.extra_end("a"), "aaa")
    def test6(self):
        self.assertEqual(self.obj.first_two("Hello"), "He")
        self.assertEqual(self.obj.first_two("abcefg"), "ab")
        self.assertEqual(self.obj.first_two(""), "")
    def test7(self):
        self.assertEqual(self.obj.first_half("WooHoo"), "Woo")
        self.assertEqual(self.obj.first_half("HelloThere"), "Hello")
        self.assertEqual(self.obj.first_half("catch"), "ca")
    def test8(self):
        self.assertEqual(self.obj.without_end("Hello"), "ell")
        self.assertEqual(self.obj.without_end("chavey"), "have")
        self.assertEqual(self.obj.without_end("zz"), "")
    def test9(self):
        self.assertEqual(self.obj.combo_string("Hello", "Hi"), "HiHelloHi")
        self.assertEqual(self.obj.combo_string('hi', 'Hello'), 'hiHellohi')
        self.assertEqual(self.obj.combo_string('aaa', ''), 'aaa')
    def test10(self):
        self.assertEqual(self.obj.non_start('Hello', 'There'), 'ellohere')
        self.assertEqual(self.obj.non_start("shot", "thead"), "hothead")
        self.assertEqual(self.obj.non_start('a', 'poops'), 'oops')
    def test11(self):
        self.assertEqual(self.obj.left2("Hello"), "lloHe")
        self.assertEqual(self.obj.left2('hi'), 'hi')
        self.assertEqual(self.obj.left2('atc'), 'cat')
#    def test12(self):
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#    def test13(self):
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
#        self.assertEqual(self.obj.)
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


