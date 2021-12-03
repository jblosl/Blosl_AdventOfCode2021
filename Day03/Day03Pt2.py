#Day03 Code Pt.2
#First part find the most common bit and least commom in each bit column and keep only the numbers with the most common bit until there is only 1 number left (Oxygen gnerator rating)
#Second part kep the numbers with the least common bit until there is only 1 number left (CO2 scrubbing Rating)
#Multiply the last most common bit value (decimal) by the last least common bit value (decimal) to get power consumption

#Initalize varaibles
lines = []
mostCommonArray = []
leastCommonArray = []
bitLowArray = []
bitHighArray = []
bitLowCount = bitHighCount = 0
bit = 0
#Read in file
with open('Day03Input.txt') as f:
    lines = f.readlines()
    
#Loop through each bit column
while bit <= 11:
    currentBit = bit
    print('Begining Length',len(lines))
    #Loop through each line
    for line in lines:
        currentLine = line
        #Check the value of bit and write the current value to an array
        if currentLine[currentBit] == "0":
            bitLowCount += 1
            bitLowArray.append(currentLine)
        else:
            bitHighCount += 1
            bitHighArray.append(currentLine)
    #Check to see if 1 or 0 is the most common and redefine lines as that
    if bitLowCount <= bitHighCount:
        lines = bitHighArray
    else:
        lines = bitLowArray
    bitHighArray = []
    bitLowArray = []
    print('End Length',len(lines))
    bit += 1  
    bitLowCount = 0
    bitHighCount = 0
    if len(lines) == 1:
        break
mostCommon = int("".join(str(x) for x in lines),2)

#------------------------------------------------------------------------#
#Reinitialize for least common
lines = []
bit = 0

#ReDefine lines to default input
with open('Day03Input.txt') as f:
    lines = f.readlines()
    
#ReLoop through each bit column
while bit <= 11:
    currentBit = bit
    print('Begining Length',len(lines))
    #Loop through each line
    for line in lines:
        currentLine = line
        #Check the value of bit and write the current value to an array
        if currentLine[currentBit] == "0":
            bitLowCount += 1
            bitLowArray.append(currentLine)
        else:
            bitHighCount += 1
            bitHighArray.append(currentLine)
    #Check to see if 1 or 0 is the least common and redefine lines as that
    if bitLowCount <= bitHighCount:
        lines = bitLowArray 
    else:
        lines = bitHighArray
    bitHighArray = []
    bitLowArray = []
    print('End Length',len(lines))
    bit += 1  
    bitLowCount = 0
    bitHighCount = 0
    if len(lines) == 1:
        break
leastCommon = int("".join(str(x) for x in lines),2)

print('oxygen generator rating:',mostCommon, '\nCO2 scrubber rating:',leastCommon)
print('life support rating:', mostCommon * leastCommon)