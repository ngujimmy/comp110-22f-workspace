"""EX03 Structured Wordle: My closest step to wordle!"""
__author__ = "730574005"


def contains_char(word: str, single_char: str) -> bool:
    """checks if character is in a word."""
    assert len(single_char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == single_char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojifies a character to green if correct, yellow if contained in the word, and white if incorrect."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
            i += 1
        else:
            if contains_char(secret, guess[i]) == True:
                emoji += YELLOW_BOX
                i += 1
            else:
                emoji += WHITE_BOX
                i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Takes your inputted guess and make sure it's the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    i: int = 1
    while i < 7 or guess == secret_word:
        print(f"=== Turn {i}/6 === ")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        i += 1
    if i == 7:
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print(f"You won in {i}/6 turns!")


if __name__ == "__main__":
    main()