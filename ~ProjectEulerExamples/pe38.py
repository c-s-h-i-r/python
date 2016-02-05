'''Project Euler 38
Take the number 192 and multiply it by each of 1, 2, and 3:
192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def isPandigital(list):
    
    ten = [0]*9
    if(len(list) != 9):
        return False
    map(int, list)    
    for i in list:
        if int(i) != 0:
            ten[int(i)-1] = 1
    for i in ten:
        if i != 1:
            return False
    return True


def getConcatenatedProduct(n):
    concatenatedProduct = ""
    i = 1
    while True:
        if len(concatenatedProduct) < 9:
            product =  int(n) * i
            concatenatedProduct += str(product)
        else:
            break;
        i += 1
    return concatenatedProduct

def getLargest():
    largest = 0
    for i in range(1,1000000):
        cp = getConcatenatedProduct(i)
        if isPandigital(cp) and cp > largest:
            largest = cp
    return largest
        
print getLargest()    

