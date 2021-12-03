#Day 01 Pt.1
#The purpose of this code is to detect if the current number hyas increased from the previous
#It needs to have a counter for how many times the number has increased

#Initalize array
lines = []

#Open File and read lines
with open('Day01Input.txt') as f:
    lines = f.readlines()

#Counter intialization
count = increaseCount =  decreaseCount = equalCount = 0

#Make the first previous vaule the same as the intial value becasue it is neither increasing or decreasing
preLine = int(lines[0])

#Loop through each line
for line in lines:
    count += 1
    currentLine = int(line) #converts the value to an int so we can use logical operators
    
    if currentLine > preLine:
        increaseCount += 1
        print(f'line {count}: {line}(increased)\n')
    elif currentLine < preLine:
        decreaseCount += 1
        print(f'line {count}: {line}(decreased)\n')
    else:
        equalCount += 1
        print(f'line {count}: {line}(maintained/no previous value)\n')

    #Store the value of the current line for the next loop
    preLine = currentLine

#Print out all the values
print('Number Increased:',increaseCount)
print('Number Decreased:',decreaseCount)
print('Number Maintained:',equalCount)
print('Total Data Points:',increaseCount + decreaseCount + equalCount)
