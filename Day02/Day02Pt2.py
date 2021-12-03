#Day02 Code Pt.2
#The purpose of this code is to track the distance and depth of a submarine
#It needs to keep track of the horizontal, vertical, and Aim
#Down/up increases/decreases the Aim by X
#Forward increases the hoirzontal postion by X and increases Depth by Aim*X

#Initalize variables
lines = []
forwardCounter = depthCoutner = aimCounter = 0

#Reading in the inputs
with open('Day02Input.txt') as f:
    lines = f.readlines()

#For loop going through inputs
for line in lines:
    currentLine = line
    #Break up the string into the two components direction and number
    splitLine = currentLine.split()

    #Tracking if it is a horizontal or vertical movement
    if splitLine[0] == "down":
        aimCounter = aimCounter + int(splitLine[1])
    elif splitLine[0] == "up":
        aimCounter = aimCounter - int(splitLine[1])
    else:
        forwardCounter = forwardCounter + int(splitLine[1])
        depthCoutner = depthCoutner + (aimCounter * int(splitLine[1]))

print('Total Distance:',forwardCounter)
print('Total Depth:',depthCoutner)
#Multiply the final distance and depth
print('Depth x Distance = ',forwardCounter*depthCoutner)      

