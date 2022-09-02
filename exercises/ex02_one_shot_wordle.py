"""EX 02 One Shot Wordle - you only got one shot, do not miss the chance to blow!"""
__author__ = "730574005"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
i: int = 0
emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
while i < len(secret):
    if guess[i] == secret[i]:
        emoji = emoji + GREEN_BOX
    else:
        j = 0
        recurring_test = "False"
        while j < len(secret):
            if guess[i] == secret[j]:
                recurring_test = "True"
            j += 1
        if recurring_test == "True":
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    i += 1

if guess == secret:
    print(emoji)
    print("Woo! You got it!")
else:
    print(emoji)
    print("Not quite. Play again soon!")