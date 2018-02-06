# Guess a secret number with option to play again

import random

while True:
    my_random_number = random.randint(1, 10)
    print("I\'m thinking of a number between 1 and 10.")
    guessRemain = 5
    exitLoop = False
    while guessRemain > 0 and exitLoop == False:
        print("You have " + str(guessRemain) + " guesses left.")
        myGuess = int(input("What\'s the number? "))
        if myGuess == my_random_number:
            print("Yes! You win!")
            exitLoop= True

        elif myGuess > my_random_number:
            print(str(myGuess) + " is too high.")
            guessRemain -= 1
            if guessRemain == 0:
                exitLoop = True
                print("You ran out of guesses!")


        else:
            print(str(myGuess) + " is too low.")
            guessRemain -= 1
            if guessRemain == 0:
                exitLoop = True
                print("You ran out of guesses!")

        
    playAgain = input("Do you want to play again (Y or N)? ")
    if playAgain == "N":
        print("Bye!")
        break
    

