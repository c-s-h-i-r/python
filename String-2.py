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
    
    @staticmethod    
    def isSubstring(a, b):
        '''a,b - strings
            return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences.
        '''
        a = a.lower()
        b = b.lower()
        if len(a) == len(b):
            return a == b

        if len(a) > len(b):
            ss = b
            pattern = a
        else:
            ss = a
            pattern = b
        
        print "len", len(pattern)-1
        for i in xrange(0, len(pattern)-1):
            if len(pattern) - i < len(ss):
                break
            if pattern[i] == ss[0]:
                print "comparing:", pattern[i:i+len(ss)],"|" , ss, "|"
                if pattern[i:i+len(ss)] == ss:
                    return True
            
        return False
    
    @staticmethod    
    def end_other(a, b):
        '''a,b - strings
            return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences.
        '''
        a = a.lower()
        b = b.lower()
        if len(a) == len(b):
            return a == b

        if len(a) > len(b):
            if a[len(a)-len(b):] == b:
                return True
            return False
        else:
            if b[len(b)-len(a):] == a:
                return True
            return False
        
    @staticmethod
    def xyz_there(str): 
        '''return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period.
        '''
        comparing = 'xyz'
        if len(str) < len(comparing):
            return False
        if len(str) == len(comparing):
            return str == comparing
        else:
            for x in xrange(0, len(str)-1):
                if str[x:x+len(comparing)] == comparing and str[x-1] != '.':
                    return True
        return False
        
        
# Here's our unit tests.
class StringTests(unittest.TestCase):
    obj = String2()
    def test1(self):
        self.assertEqual(self.obj.end_other('Hiabc','abc'), True)
        self.assertEqual(self.obj.end_other('abC','HiaBc'), True)
        self.assertEqual(self.obj.end_other('abc','abXabc'), True)
        self.assertEqual(self.obj.end_other('Hiabcx','bc'), False)
        self.assertEqual(self.obj.end_other('ab','ab12'), False)
        self.assertEqual(self.obj.end_other('abc','abXabc'), True)
    def test2(self):
        self.assertEqual(self.obj.xyz_there('abcxyz'), True)
        self.assertEqual(self.obj.xyz_there('abc.xyz'), False)
        self.assertEqual(self.obj.xyz_there('xyz.abc'), True)
        self.assertEqual(self.obj.xyz_there(''), False)
        self.assertEqual(self.obj.xyz_there(''), False)
        self.assertEqual(self.obj.xyz_there(''), False)
    def test2(self):
        self.assertEqual(self.obj.xyz_there(''), False)
        self.assertEqual(self.obj.xyz_there(''), False)
        self.assertEqual(self.obj.xyz_there(''), False)
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
                    




    


