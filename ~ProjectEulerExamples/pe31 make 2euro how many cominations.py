''' Project Euler 31
In England the currency is made up of pound and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, 1euro (100p) and 2euro (200p).
It is possible to make 2euro in the following way:

1x1E + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can 2E be made using any number of coins?
'''

def make2Euro(startIndex, coinLimit):
    coins = [1,2,5,10,20,50,100,200]
    coinsUsed = [0]*len(coins)
    amountToMake = 200
    
    
    for i in range(startIndex,-1,-1):
    
        while amountToMake > 0 and coinsUsed[i] <= coinLimit[i]:
            
                if(amountToMake >= coins[i]):
                    amountToMake -= coins[i]
                    coinsUsed[i] += 1
                else:
                    break
                
    return coinsUsed
def allWays():
    list = []
    coinLimit = [0,0,0,0,0,0,0,0]
    
    for j in range(1, 200):
        
        for i in range(7):
            coinLimit[i] = j
            print "making 2 euro with", coinLimit, i
            list.append(make2Euro(i, coinLimit))

    return list, len(list)
    
result = allWays()
print result[0]
print result[1]
