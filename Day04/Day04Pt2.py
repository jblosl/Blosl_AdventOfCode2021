#Day04 Code Pt.2
#BINGO there are a set of 5x5 bingo cards that need to be checked and marked as numbers are drawn
#Determine which BINGO card is going to win last (the most amount of nuumbers called)
#Once the winner is determined find the score by adding all unmarked numbers and multiply that sum by the last number drawn

import numpy as np

#Initalize varaibles
lines = []
BINGO = np.array(['!', '!', '!', '!', '!'])
BINGOcheck = np.array([['!', '!', '!', '!', '!'],['!', '!', '!', '!', '!'],['!', '!', '!', '!', '!'],['!', '!', '!', '!', '!'],['!', '!', '!', '!', '!']])
bingoCounter = 0
FirstBingoCount = 0
startLine = 2
endLine = 7
cardNumber = 1

#Read in file
with open('Day04/Day04Input.txt') as f:
    lines = f.readlines()
    
#Extract the call numbers
callNumbers = lines[0].split(",")

#Loop through each bingo card
while endLine <= len(lines):
    #Extract the bingo card and separate it into rows
    bingoCard = lines[startLine:endLine]
    Row1 = np.array(bingoCard[0].split())
    Row2 = np.array(bingoCard[1].split())
    Row3 = np.array(bingoCard[2].split())
    Row4 = np.array(bingoCard[3].split())
    Row5 = np.array(bingoCard[4].split())
    rowArr = np.vstack((Row1,Row2,Row3,Row4,Row5))

    #Check each call number and mark any numbers called with a !
    for callNum in range(len(callNumbers)):
        currentCallNum = callNumbers[callNum]
        rowArr = np.where(rowArr == currentCallNum, '!', rowArr)
        bingoCounter += 1
        ''
        #Check to see if there is a bingo in any of the rows of the card
        if np.array_equal(rowArr[0],BINGO) == True or np.array_equal(rowArr[1],BINGO) == True or np.array_equal(rowArr[2],BINGO) == True or np.array_equal(rowArr[3],BINGO) == True or np.array_equal(rowArr[4],BINGO) == True:
            print('--------------------------')
            print('Card Number:', cardNumber)
            print('Row Bingo')
            print('Bingo Counter:',bingoCounter)
            #See if bingo was achieved faster than any of the previous cards
            if bingoCounter > FirstBingoCount:
                FirstBingoCount = bingoCounter
                print(rowArr)
                print('Current Call Num:', currentCallNum)
                leftOverNums = (np.setdiff1d(rowArr, BINGOcheck)).astype(float)
                #Calculate the sum of the numbers remaining on the card and multiple by the number that made BINGO
                print('Sum of leftover numbers:',np.sum(leftOverNums))
                print('Final Answer:',np.sum(leftOverNums)*int(currentCallNum))
            #Once BINGO is achieved break the loop and move onto the next card
            break
        columnArr = np.transpose(rowArr)
        #Check to see if there is a bingo in any of the columns of the card
        if np.array_equal(columnArr[0],BINGO) == True or np.array_equal(columnArr[1],BINGO) == True or np.array_equal(columnArr[2],BINGO) == True or np.array_equal(columnArr[3],BINGO) == True or np.array_equal(columnArr[4],BINGO) == True:    
            print('--------------------------')
            print('Card Number:', cardNumber)
            print('Column Bingo')
            print('Bingo Counter:', bingoCounter)
            #See if bingo was achieved faster than any of the previous cards
            if bingoCounter > FirstBingoCount:
                FirstBingoCount = bingoCounter
                print(rowArr)
                print('Current Call Num:', currentCallNum)
                leftOverNums = (np.setdiff1d(rowArr, BINGOcheck)).astype(float)
                #Calculate the sum of the numbers remaining on the card and multiple by the number that made BINGO
                print('Sum of leftover numbers:',np.sum(leftOverNums))
                print('Final Answer:',np.sum(leftOverNums)*int(currentCallNum))
            #Once BINGO is achieved break the loop and move onto the next card
            break
    #Reset the counter that teracks how many numbers are called
    bingoCounter = 0
    #Increment the start and endline as well as the card number
    startLine += 6
    endLine += 6
    cardNumber += 1
