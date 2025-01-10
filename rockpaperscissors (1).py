#Init

import random
playerScore = 0
computerScore = 0
playing = 1
deciding = 1

#Functions

def rpc_selector():
    global playing
    while playing == 1:
        #Always runs unless player quits
        global deciding
        while deciding == 1:
            global playerScore
            global computerScore

            #introduction

            print("Current score is: PLAYERr " + str(playerScore) + " - " + str(computerScore) + " COMPUTER")
            print("Select 'rock', 'paper', or 'scissors', or type 'quit' to quit!")
            playerSelected = str(input())
            playerSelected.casefold()

            #If player quits, program stops.
            #If player enters an invalid input, repeats until a valid input is entered

            if playerSelected == "quit":
                playing = 0
                deciding = 0

            elif playerSelected == "rock" or playerSelected == "paper" or playerSelected == "scissors":
                deciding = 0

            else:
                print("""ENTER A VALID INPUT!
                      """)
                deciding = 1

        #converts ints to strings

        computerInteger = random.randint(1,3)
        if computerInteger == 1:
            computerSelected = "rock"
        elif computerInteger == 2:
            computerSelected = "paper"
        elif computerInteger == 3:
            computerSelected = "scissors"

            #ALL winner determination.
            #First is if code for when player wins. In that case, a point is awarded to the player
            #Second is code for when player loses. In that case, a point is awarded to the computer
            #Third is when they tie. No points are awarded.

        if (computerSelected == "rock" and playerSelected == "paper") or (computerSelected == "paper" and playerSelected == "scissors") or (computerSelected == "scissors" and playerSelected == "rock"):
            print("")
            print("You selected " + '\033[1m' + str(playerSelected.capitalize()) + '\033[0m')
            print("Computer selected " + '\033[1m' + str(computerSelected.capitalize()) + '\033[0m')
            print("")
            print('\033[1m' + "You Win!" + '\033[0m' + " 1 point has been added to your score!")
            playerScore = playerScore + 1
        elif (computerSelected == "rock" and playerSelected == "scissors") or (computerSelected == "paper" and playerSelected == "rock") or (computerSelected == "scissors" and playerSelected == "paper"):
            print("")
            print("You selected " + '\033[1m' + str(playerSelected.capitalize()) + '\033[0m')
            print("Computer selected " + '\033[1m' + str(computerSelected.capitalize()) + '\033[0m')
            print("")
            print('\033[1m' + "You Lost!" + '\033[0m' + " 1 point has been added to the computer's score!")
            computerScore = computerScore + 1
        elif (computerSelected == "rock" and playerSelected == "rock") or (computerSelected == "paper" and playerSelected == "paper") or (computerSelected == "scissors" and playerSelected == "scissors"):
            print("")
            print("You selected " + '\033[1m' + str(playerSelected.capitalize()) + '\033[0m')
            print("Computer selected " + '\033[1m' + str(computerSelected.capitalize()) + '\033[0m')
            print("")
            print('\033[1m' + "You Tied!" + '\033[0m' + " No points have been gained!")

        deciding = 1



#Main

print("Welcome to rock, paper, scissors!")

#Always runs unless palyer quits.
while playing == 1:
    rpc_selector()
