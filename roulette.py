####################
# Carlysse Nycole Castro
# Program 1 - Roulette Simulator 
# CS 320 - Summer 2021
####################
import random

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to the game of R O U L E T T E")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
table = input("Which table would you like to play on? (American or European)? ")
print("\n")
min = int(input("Please enter your minimum bet amount: "))
print("\n")
betLimit = int(input("Please enter your maximum bet amount: ")) 
print("\n")
spins = int(input("Please enter amount of spins you would like to do: ")) 
print("\n")

if (table == "American"): 
    isAmerican = True
else: 
    isAmerican = False 

# Global variables that will be used for win/loss functions
betAmount = min
netWinnings = 0
maxWinnings = 0
maxLoss = 0
numWon = 0
numLoss = 0
avgWin = 0
avgLoss = 0 
currentLoss = 0


# main funtion: Runs roulette simulator
def main(): 
    # Loops until reaches desired amount of spins or until betLimit is reached
    for i in range (spins): 
        spin()

        if (betAmount >= betLimit): 
            break

        if (spin() == True): 
            win()
        else: 
            lose()

    printResults()

# Win function: handles calculations involved with the results of winning
def win():
    global netWinnings
    global betAmount
    global maxWinnings
    global avgWin
    global currentLoss
    global numWon

    netWinnings = netWinnings + betAmount
    if (betAmount > maxWinnings): 
        maxWinnings = betAmount

    avgWin = avgWin + betAmount
    betAmount = min
    currentLoss = 0
    numWon += 1

# Lose funtion: handles calculations involved with the results of losing
def lose(): 
    global currentLoss
    global betAmount
    global netWinnings
    global maxLoss
    global avgLoss
    global numLoss

    netWinnings = netWinnings - betAmount

    currentLoss = currentLoss + betAmount
    if (currentLoss > maxLoss):
        maxLoss = currentLoss

    avgLoss = avgLoss + betAmount
    betAmount = currentLoss
    numLoss += 1

# spin function: "spins roulette" and gets color of the slot that was landed on 
def spin():
    if isAmerican:
        slotNum = random.randint(1, 38)
        isBlack = getColor(slotNum)
        return isBlack
    else: 
        slotNum = random.randint(1, 37)
        isBlack = getColor(slotNum)
        return isBlack

# getColor function: returns the color of the number that was landed on from the spin function 
# Depending on the certain group of numbers, each set is either odds = red / evens = black 
# or evens = red / odds = black 
def getColor(number): 
    if (number >= 1 and number <= 10):
        color = number % 2
        if (color == 0): 
            isBlack = True
        else: 
            isBlack = False
        
        return isBlack

    if (number >= 19 and number <= 28): 
        color = number % 2
        if (color == 0):
            isBlack = True
        else:
            isBlack = False

        return isBlack

    if (number >= 11 and number <= 18): 
        color = number % 2
        if (color != 0):
            isBlack = True
        else: 
            isBlack = False

        return isBlack
            
    if (number >= 29 and number <= 36):
        color = number % 2
        if (color != 0):
            isBlack = True
        else:
            isBlack = False
        
        return isBlack 

    if (number > 36): 
        isBlack = False 
        return isBlack 

# printResults: prints out the results of the game
def printResults(): 
    print(" ~ ~ ~ ~ RESULTS ~ ~ ~ ~\n")
    print('NET WINNINGS: {:>15}'.format(netWinnings))
    print('GREATEST PAYOUT: {:>12}'.format(maxWinnings))
    print('GREATEST LOSS: {:>14}'.format(maxLoss))
    print('ROUNDS WON: {:>17}'.format(numWon))
    print('ROUNDS LOSS: {:>16}'.format(numLoss))
    formatAvgWin = "{:.2f}".format(avgWin/numWon)
    formatAvgLoss = "{:.2f}".format(avgLoss/numLoss)
    print('AVG PAYOUT: {:>17}'.format(formatAvgWin))
    print('AVG LOSS: {:>19}'.format(formatAvgLoss))


# Initiates roulette simulator        
main()
