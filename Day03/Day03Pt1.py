#Day03 Code Pt.1
#find the most common bit and least commom in each bit column
#Multiply the most common bit (decimal) by the least common bit (decimal) to get power consumption

#Initalize varaibles
lines = []
mostCommonArray = []
leastCommonArray = []
bitHighArray = []
bitLowCount = bitHighCount = 0

#Read in file
with open('Day03/Day03Input.txt') as f:
    lines = f.readlines()

#Loop through each bit column
for bit in range(0,12,1):
    currentBit = bit 
    #Loop through each line
    for line in lines:
        currentLine = line
        #Check the value of bit
        if currentLine[currentBit] == "0":
            bitLowCount += 1
        else:
            bitHighCount += 1
    #Add proper values to the most and least common binary values
    if bitLowCount > bitHighCount:
        mostCommonArray.append(0)
        leastCommonArray.append(1)
    else:
        mostCommonArray.append(1)
        leastCommonArray.append(0)
    #Reinintalize values for next loop
    bitLowCount = 0
    bitHighCount = 0    
        
print(mostCommonArray, leastCommonArray)          
#convert final biinary number to decimal
leastCmnDec = int("".join(str(x) for x in leastCommonArray),2)
mostCmnDec = int("".join(str(x) for x in mostCommonArray),2)
print('The most common deicmal value:',mostCmnDec, '\nThe least common decimal value:', leastCmnDec)
#multiply most and least common together
finalProduct = leastCmnDec * mostCmnDec
print('Most Common * Least Common = ', finalProduct)