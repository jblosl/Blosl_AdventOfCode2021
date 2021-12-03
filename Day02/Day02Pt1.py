#Day02 Code Pt.1
#The purpose of this code is to track the distance and depth of a submarine
#It needs to keep track of both the horizontal and vertical movement and at th3e end multiply the two together

#Initalize variables
lines = []
forwardCounter = depthCoutner = 0

#Reading in the inputs
with open('Day02Input.txt') as f:
    lines = f.readlines()

#For loop going through inputs
for line in lines:
    currentLine = line
    #Break up the string into the two components direction and number
    splitLine = currentLine.split()

    #Tracking if it is a horizontal or vertical movement
    if splitLine[0] == "forward":
        forwardCounter = forwardCounter + int(splitLine[1])
    elif splitLine[0] == "up":
        depthCoutner = depthCoutner - int(splitLine[1])
    else:
        depthCoutner = depthCoutner + int(splitLine[1])

print('Total Distance:',forwardCounter)
print('Total Depth:',depthCoutner)
#Multiply the final distance and depth
print('Depth x Distance = ',forwardCounter*depthCoutner)      

