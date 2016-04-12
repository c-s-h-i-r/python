"""Write a program that prints the numbers from 1 to 100. But for multiples 
    of three print Fizz instead of the number and for the multiples of 
    five print Buzz. 
    For numbers which are multiples of both three and five print FizzBuzz.
"""

def fizzBuzz(n):
    '''n is the limit of the series to print
    '''
    for i in range(1, n+1):
        toPrint = ''
       
        if i % 3 == 0:
            toPrint = "Fizz"
        if i % 5 == 0:
            toPrint += 'Buzz'
        print toPrint if toPrint != '' else i


def main():
    fizzBuzz(100)    
    
if __name__ == '__main__':
    main()                    