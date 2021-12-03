#Day 01 Pt. 2
#The purpoise of this code is to detect if the sum of the current 3 number array have increased from the sum of the previous 3 number array
#Ex: A(199, 200, 208) and B(200, 208, 210)
#   The sume of A is 607 and B is 618 so the first comparison increased
#It needs to have a counter for how many times the number has increased

#Initalize array
lines = []

#Open File and read lines
with open('Day01Input.txt') as f:
    lines = f.readlines()

#Counter intialization
count = increaseCount =  decreaseCount = equalCount = 0

#Line Counters
slot1 = 0
slot2 = 1
slot3 = 2
previousArraySum = int(lines[slot1]) + int(lines[slot2]) + int(lines[slot3])
letterCounter = 'A'

#Loop through each line
while slot3 <= len(lines)-1:
    currentArraySum = int(lines[slot1]) + int(lines[slot2]) + int(lines[slot3])
    
    if currentArraySum > previousArraySum:
        increaseCount += 1
        print(letterCounter,': ', currentArraySum,' (increased)\n')
    elif currentArraySum < previousArraySum:
        decreaseCount += 1
        print(letterCounter,': ', currentArraySum,' (decreased)\n')
    else:
        equalCount += 1
        print(letterCounter,': ', currentArraySum,' (equal no previous value)\n')
        
    #Store the previous sum for the next loop
    previousArraySum = currentArraySum

    #Increments the slots
    slot1 += 1
    slot2 += 1
    slot3 += 1
    # #Increments the letter
    # letterCounter = chr(ord(letterCounter) + 1)

#Print out all the values
print('Number Increased:',increaseCount)
print('Number Decreased:',decreaseCount)
print('Number maintained:',equalCount)
print('Total Data Points:',increaseCount + decreaseCount + equalCount)
