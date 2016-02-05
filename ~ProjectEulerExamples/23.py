from sets import Set

def Divs(Number):
    Divisors = []

    for i in range(2 , int(Number**0.5) + 1):
        if Number % i == 0:
            Divisors.append(i)

    for q in range(len(Divisors)):
        if Divisors[q] != (Number / Divisors[q]):
            Divisors.append(Number / Divisors[q])

    Divisors.insert(0,1)
    return Divisors

#returns a list of abundant numbers up to and including the limit
def AbList(limit):
    Abundant = Set()

    for i in range(11,limit + 1):
        if sum(Divs(i)) > i:
            Abundant.add(i)

    return Abundant

#Finds the sum of all positive integers that cannot be written as the
#sum of two abundant numbers...
def AbSum(limit):
    Abundant = AbList(limit)
    NoAbSum = 0
    for i in range(1 , limit):
        AbSum = 0
        
        for x in Abundant:
            if i - x in Abundant:
                AbSum = 1
                break
        if AbSum == 0:
            NoAbSum += i
    return NoAbSum
print AbSum(28123)