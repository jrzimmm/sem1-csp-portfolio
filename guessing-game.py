#Init

import random

#Functions

#Main
chips = 100

playAgain = True

#Always runs unless chips < 10
while playAgain and chips >= 10:

    #Introduction & setup

    print("RANDOM NUMBER GUESSING GAME!")
    print("")
    print("THIS GAME COSTS 10 CHIPS TO PLAY!")
    print("")
    print("You currently have", chips ,"CHIPS")
    print("")
    print("Select EASY, MEDIUM, or HARD (type in lowercase)")

    #Resets number of guesses used to 0
    numGuessCount = 0

    diffSelect = False

    #Always runs until a valid difficulty is selected.
    while not diffSelect:
        diffSelected = input()
        if diffSelected == "easy":

            #Easy difficulty (0-10 guess)

            actNumber = random.randint(0,10)
            chips = chips - 10
            print("Pick a random number between 0 and 10 (ENTER INTEGERS ONLY)")
            print("")
            diffSelect = True

            numGuess = False
            while not numGuess:
                numAnswer = input()

                #If correct number guessed
                if int(numAnswer) == actNumber:
                    print("CONGRATS!!! You guessed the correct number and won 5 chips!")
                    chips = chips + 15
                    numGuess = True
                else:
                    numGuessCount = numGuessCount + 1
                    if numGuessCount < 3:
                        print("Sorry," , numAnswer , "is not correct! You have" , 3-numGuessCount , "guesses left.")
                    else:
                        print("Sorry," , numAnswer , "is not correct!" , actNumber , "was the correct number :(")
                        numGuess = True


        elif diffSelected == "medium":


            #Medium difficulty (0-25 guess)
            actNumber = random.randint(0,25)
            chips = chips - 10
            print("Pick a random number between 0 and 25 (ENTER INTEGERS ONLY)")
            print("")
            diffSelect = True

            numGuess = False
            while not numGuess:
                numAnswer = input()
                if int(numAnswer) == actNumber:
                    print("CONGRATS!!! You guessed the correct number and won 25 chips!")
                    chips = chips + 35
                    numGuess = True
                else:
                    numGuessCount = numGuessCount + 1
                    if numGuessCount < 3:
                        print("Sorry," , numAnswer , "is not correct! You have" , 3-numGuessCount , "guesses left.")
                    else:
                        print("Sorry," , numAnswer , "is not correct!" , actNumber , "was the correct number :(")
                        numGuess = True

        elif diffSelected == "hard":

            #Hard difficulty (0-100 guess)

            actNumber = random.randint(0,100)
            chips = chips - 10
            print("Pick a random number between 0 and 100 (ENTER INTEGERS ONLY)")
            print("")
            diffSelect = True

            numGuess = False
            while not numGuess:
                numAnswer = input()
                if int(numAnswer) == actNumber:
                    print("CONGRATS!!! You guessed the correct number and won 150 chips!")
                    chips = chips + 160
                    numGuess = True
                else:
                    numGuessCount = numGuessCount + 1
                    if numGuessCount < 3:
                        print("Sorry," , numAnswer , "is not correct! You have" , 3-numGuessCount , "guesses left.")
                    else:
                        print("Sorry," , numAnswer , "is not correct!" , actNumber , "was the correct number :(")
                        numGuess = True

    #When round ends, if the player quits, the code will stop.
    #If the player wants to play again but they have <10 chips, they lose thegame and the code stops.

    print("Play again? Type 'yes' to play again. Type anything else to close the program.")
    playingAgain = input()
    if playingAgain != "yes":
        playAgain = False
    elif playingAgain == "yes" and chips >= 10:
        print("Lets play again, shall we?")
        print("")
        print("")
        print("")
    elif playingAgain == "yes" and chips < 10:
        print("You're out of chips! That's why you don't gamble!")

