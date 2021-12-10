#Day05 Code Pt.1
#find where the hydrothermal vents
#The vents will be in a line based on the two input points
#Only consider the horizontal and vertical lines right now (no need to worry about slope)

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
        
    #If it is neither a horizontal nor vertical line that means it is diagnol and move to the next set of numbers
    else:
        continue

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