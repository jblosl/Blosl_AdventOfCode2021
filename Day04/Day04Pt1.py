#Day04 Code Pt.1
#BINGO there are a set of 5x5 bingo cards that need to be checked and marked as numbers are drawn
#Once the winner is determined find the score by adding all unmarked numbers and multiply that sum by the last number drawn

#Initalize varaibles
lines = []


#Read in file
with open('Day04Input.txt') as f:
    lines = f.readlines()

#Extract the call numbers
callNumbers = lines[1]
print(callNumbers)

#Extract the bingo cards

#Check each bingo card against the call numbers

    #track how many nubers it took and keep only the one that had the least

#Sum all the unmarked numbers and multioply by the last call number needed for BINGO