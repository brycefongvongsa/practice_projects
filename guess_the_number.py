import random, sys

## setup
secretNum = random.randint(1, 100)
numOfTries = 6
userInput = 0

# start of game
print("\nGuess the number from 1 to 50!")
print(f"You have {numOfTries} attempts.")
while numOfTries != 0:
    userInput = int(input())
    if userInput > 100 or userInput < 0:
        print("it not within range pls try again")
    else:  
        if userInput != secretNum:
            numOfTries = numOfTries - 1
            if userInput > secretNum:
                print(f"Guess lower. You have {numOfTries} tries left.")
            elif userInput < secretNum:
                print(f"Guess higher. You have {numOfTries} tries left.")
        else:
            sys.exit("Good job! You guessed right!")
            
## game over, end game
if numOfTries == 0:
    sys.exit(f"Game over. The number was {secretNum}.")

    
