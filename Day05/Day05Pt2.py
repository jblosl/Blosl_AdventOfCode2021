#Day05 Code Pt.2
#find where the hydrothermal vents
#The vents will be in a line based on the two input points
#Now we need to consider both horizontal and vertical lines as well as the diagnols

from types import MappingProxyType
import numpy as np

#Initialize Variables
lines = []
minValueX = 100
maxValueX = 0
minValueY = 100
maxValueY = 0
MappedArray = np.zeros((990, 990),dtype=int)
multiCounter = 0

#Read in file
with open('Day05/Day05Input.txt') as f:
    lines = f.readlines()
  
for line in lines:
    #Extract only the numbers
    currentLine = line
    current = (np.array(currentLine.split(','))).astype(int)
    
    #Check to see if the X values stayed constant, meaning a vertical line is present
    if current[0] == current[2]:
        print('\nVertical Line \nX Value:',current[0], '\nY Range:',current[1], current[3])
        if current[1] < current[3]:
            verticalLineArr = list(range(current[1], current[3]+1))
        else:
            verticalLineArr = list(range(current[3], current[1]+1))
        for nums in range(len(verticalLineArr)):
            MappedArray[current[0],verticalLineArr[nums]] = MappedArray[current[0],verticalLineArr[nums]] + 1
        # print('vertical Line Length:',verticalLineArr)
        
    #Check to see if the Y values stayed constant, meaning a horizontal line is present
    elif current[1] == current[3]:
        print('\nHorizontal Line \nY Value:',current[1], '\nX Range', current[0], current[2])
        if current[0] < current[2]:
            horizontalLineArr = list(range(current[0],current[2]+1))
        else:
            horizontalLineArr = list(range(current[2],current[0]+1))
        for nums in range(len(horizontalLineArr)):
            MappedArray[horizontalLineArr[nums],current[1]] = MappedArray[horizontalLineArr[nums],current[1]] + 1
        # print('Horizontal Line Length:', horizontalLineArr)
        
    #If it is neither a horizontal nor vertical line that means it is diagnol
    else:
        print('\nDiagnol Line \nX Range:',current[0], '-', current[2], '\nY Range:', current[1], '-', current[3])
        #Find the X Range
        if current[0] < current[2]:
            xRange = list(range(current[0],current[2]+1))
        else:
            xRange = list(range(current[0],current[2]-1,-1))
        #Find the Y Range
        if current[1] < current[3]:
            yRange = list(range(current[1], current[3]+1))
        else:
            yRange = list(range(current[1], current[3]-1,-1))
        #Go through each pair of points for the diagnol line and add 1 to that spot on the Mapped Array
        for diagNums in range(len(xRange)):
            MappedArray[xRange[diagNums],yRange[diagNums]] = MappedArray[xRange[diagNums],yRange[diagNums]] + 1

#Go through each row of the marked map
for rows in range(len(MappedArray)):
    currentRow = MappedArray[rows]
    #Go through each number in the row
    for numbers in range(len(currentRow)):
        currentNumber = currentRow[numbers]
        #Check to see if there is at least two or more lines overlapping
        if currentNumber >= 2:
            multiCounter += 1
        else:
            continue
print('Number of muliLine Values:',multiCounter)