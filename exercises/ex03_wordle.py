"""EX03 Structured Wordle: My closest step to wordle!"""
__author__ = "730574005"


def contains_char(word: str, single_char: str) -> bool:
    """Checks if character is in a word."""
    assert len(single_char) == 1
    i: int = 0
    while i < len(word):
        # checks if word has the single_character in it and returns True if so
        if word[i] == single_char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojifies a character to green if correct, yellow if contained in the word, and white if incorrect."""
    assert len(guess) == len(secret)
    # unicode for boxes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            # if the i letter of guess is equal to the i letter of secret it makes it a green box
            emoji += GREEN_BOX
            i += 1
        else:
            if contains_char(secret, guess[i]) is True:
                # uses contains_char function and checks if a letter of guess is in secret and assigns a yellow box
                emoji += YELLOW_BOX
                i += 1
            else:
                # assigns a white box if the letter in guess wasn't found in secret
                emoji += WHITE_BOX
                i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Takes your inputted guess and make sure it's the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        # checks to see if length of guess is the correct length to whatever secret is
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    i: int = 1
    while i < 7 and guess != secret_word:
        # while loop checks if counter is below 7 tries and if guess is not equal to secret word
        print(f"=== Turn {i}/6 === ")
        # counts turns
        guess = input_guess(len(secret_word))
        # assign's guess variable to user input
        print(emojified(guess, secret_word)) 
        # emojifies the guess to secret word
        i += 1
    if i == 7:
        return print("X/6 - Sorry, try again tomorrow!")
    else:
        return print(f"You won in {i - 1}/6 turns!")


if __name__ == "__main__":
    main()