'''Project Euler 42 Triangle Words
The nth term of the sequence of triangle numbers is given by, tn = 1/2 n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 

For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, how many are triangle words?
'''
class pe42:

    wordDict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26 
    }
    
    triangleNumbers = []
    
    def readWords(self):	
		f = open('p042_words.txt', 'r')
		text = f.read()
		words = text.split(" ")
		print words

    def wordValue(self,str):
        sum = 0
        for i in str:
            sum += self.wordDict[i]
        return sum
    def getTriangleNumbers(self):
        for i in range(1, 400):
            num = int(i**0.5) * (i+1)
            self.triangleNumbers.append(num)
        
    def main(self):
		#self.readWords()
        print self.getTriangleNumbers()#self.wordValue('abc')

		
		
		
if __name__ == "__main__":
    c = pe42()
    c.main()