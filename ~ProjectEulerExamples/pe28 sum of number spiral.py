'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def createSpiral(colcount,rowcount):
	#start at 1001
    row = 0
    col = colcount-1
    top = colcount * rowcount
    matrix = [[0 for x in range(colcount)] for x in range(rowcount)]
    level = 0
    colstep = -1    
    #make first row
    for i in range(colcount-level):
        matrix[row][col] = top
        col += colstep 
        top -= 1
    level += 1
    #printMatrix(matrix)
    
    col += 1 # revert the extra minus on column to make it positive
    colskip = True
    rowstep = 1
    rowskip = False
    while top > 0:
        #increase the level
        for j in range(2):
            #row first
            #print "colcount-level = %d %d %d" %(colcount,level,colcount-level)
            #print row,col, rowskip, colskip, rowstep, colstep
            for i in range(colcount-level):
                if not rowskip:
                    row += rowstep
                if not colskip:
                    col += colstep
                
                matrix[row][col] = top
                top -= 1
       #         printMatrix(matrix)
                
            if  colskip:
                colstep *= -1
            if  rowskip:
                rowstep *= -1
            colskip = not colskip    
            rowskip = not rowskip
        level += 1
    return matrix

def findDiagonalSum(matrix, length):
    '''finds sum of both diagonals of square matrix '''
    sum = 0
    j = 0
    for i in range(length):
        sum += matrix[i][i]
    for i in range(length-1, -1, -1):
        sum += matrix[j][i]
        j += 1
    return sum-1
    
def printMatrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))
    print "-------------------------"
        
mat = createSpiral(1001,1001)
print findDiagonalSum(mat, 1001)

        