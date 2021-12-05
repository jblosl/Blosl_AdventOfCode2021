#Day04 Code Pt.1
#BINGO there are a set of 5x5 bingo cards that need to be checked and marked as numbers are drawn
#Once the winner is determined find the score by adding all unmarked numbers and multiply that sum by the last number drawn

#Initalize varaibles
lines = []

import numpy as np
checkedCard = np.zeros([5,5])

#Read in file
with open('Day04/Day04Input.txt') as f:
    lines = f.readlines()
    
#Extract the call numbers
callNumbers = lines[0].split(",")
print(callNumbers)

#Extract the bingo cards
bingoCard = lines[2:7]
print(bingoCard)
j = 0
for rowNumbers in range(len(bingoCard)):
    BingoCardNumbers = bingoCard[rowNumbers].split()
    print(BingoCardNumbers)
    #Check each bingo card against the call numbers
    for nums in range(len(callNumbers)):
        currentCallNum = callNumbers[nums]
        for i in range(len(bingoCard)):
            currentBingoNum = BingoCardNumbers[i]
            if currentCallNum == currentBingoNum:
                checkedCard[j,i] = currentBingoNum
        for 
        if checkedCard
        # print(checkedCard)
    print(j)
    j += 1   
print(checkedCard)


    #track how many nubers it took and keep only the one that had the least

#Sum all the unmarked numbers and multioply by the last call number needed for BINGO