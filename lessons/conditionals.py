"""An example of conditions (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have wonderful day!!!")
else: 
    print("Sorry, you guess incorrectly :(")
    print("Try running the program again.")

print("Game over.")