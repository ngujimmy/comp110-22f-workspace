"""Choose You Own Adventure!"""

__author__ = "730574005"

from random import randint
points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001F633"


def greet() -> None:
    """Greets player."""
    global player
    print("Welcome to Romance Dating Simulator")
    player = input("Begin by inputting your Name: ")
    if player == "":
        print("Please input a name")
        greet()


def ending(end: int) -> int:
    """Ending is chosen depending on amount of points."""
    if end == 3:
        print(f"I love you too {player} I hope we can be happy forever!!")
        return end + 1
    else:
        print("Kris: Sorry I don't think we are compatible, contact me some other time...")
        return end


def pathway1() -> None:
    """Starts the 1st pathway where you go on a date."""
    global points
    points += 1
    choice: str = ""
    print(f"Kris: Ohh.. uhh thanks!, I think you're really cute too {player} {NAMED_CONSTANT}")
    choice = input(f"1. Would you like to go on a date with me? {NAMED_CONSTANT}\n2. Would you go out with me? {NAMED_CONSTANT}\n")
    if choice == "1":
        points += 1
        print("Kris: I would love to go on a date with you, where should we go?")
    else:
        points -= 1
        print("Kris: Uhh, that made me a bit uncomfortable but I like your honesty")
        print("Kris: We should go on a date first")
        print("Kris: Where should we go?")
    wheel: int = 1
    print("Kris: Actually I have an idea, why don't we spin a number wheel and see where it lands")
    print("Kris: If it lands on 1 we will go to a resturant if it lands on 2 we can chill at my place")
    print("'Kris gets a number wheel from his back pocket and spins it'")
    wheel = randint(1, 2)
    print(f"Kris: It seems that the wheel landed on {wheel}")
    if wheel == 1:
        print("Kris: Lets go to a nice resturant then\n")
        print("'You and Kris go to Chic-fil-a to eat'\n")
        print("While you are eating what do you decide to do?")
        choice = input("1. You drop your food on the floor and eat it\n2. You make nice conversation and have fun")
        if choice == "1":
            points -= 1
            print("\nKris: EWWW gross! how could you eat off the floor")
        else:
            points += 1
            print(f"\nKris: LOL, that was so funny {player}")
        print(f"Kris: That date was really {player}")
        print("'You finally get the courage to ask Kris out")
        print(f"{player}: Kris.. I think I really love you {NAMED_CONSTANT}")
        points = ending(points)
    else:
        print("Kris: Lets go to my place, I can probably make us something to eat\n")
        print("You guys go out together towards his place as he makes you food")
        print("While you are at his place what do you do")
        choice = input("1. You run around like a child\n2. You guys have a nice time eating while talking about your day")
        if choice == "1":
            points -= 1
            print("\nKris: What are you doing? Running around like a child.")
        else:
            points += 1
            print(f"\nKris: LOL, that was so funny {player}")
        print("The rest of the night goes normal")
        print(f"Kris: That date was really {player}")
        print("'You finally get the courage to ask Kris out")
        print(f"{player}: Kris.. I think I really love you {NAMED_CONSTANT}")
        points = ending(points)


def pathway2() -> None:
    """Starts the 2nd pathway where you talk about the assignment."""
    global points
    choice: str = ""
    print("Kris: Yeah sure what do you need help with?")
    choice = input("1. I think I need help with this! 'shows undergarments'\n2. I was wondering If I needed an f string in this piece of code")
    if choice == "1":
        points = 0
        print("Kris: EWWW!! Gross.. Get away from me I'm calling the police")
        return
    else:
        points += 1
        print("Kris yeah you do right here\n")
        print("Kris Jordan reaches close to you, you blush a bit as his arm touches yours")
        choice = input("1. Kris get away from me!!\n2. Hey, I think you're touching me")
        if choice == "1":
            points -= 1
            print("Kris: Sorry I was just trying to help")
        else:
            points += 1
            print(f"Kris:{NAMED_CONSTANT} Sorry I didn't realize I was touching you")
        print("Well anyway here you go and it seems like your code is now working")
        choice = input("1. Thank you so much!!\n2. Whatever, thanks I guess")
        if choice == "1":
            points += 1
            print("Kris: You are very welcome")
        else:
            points -= 1
            print("Kris: How rude of you")
        print("Kris: Well that was fun, tell me if you need anything else")
        print(f"{player}: Well actually, I was wondering if you would go out with me")
        print(f"{player}: I think I really love you!")
        points = ending(points)


def main() -> None:
    """Entrypoint to starting dating sim."""
    global points
    greet()
    choice: str = ""
    print("The scene is set, You see Kris Jordan walk out of Hamilton Hall and walk up to him")
    print(f"Kris: Hey {player} whats up?")
    choice = input("1. 'Hey cutie' \n2. 'I have a question about the assignment'\n3. Never mind, I think I'm gonna walk away\n")
    if choice == "1":
        pathway1()
    elif choice == "2":
        pathway2()
    else:
        print("You walk away never to face Kris Jordan again.")
    choice = input("Would you like to play again?\n1. 'Yes of course!'\n2. 'Nah'\n")
    if choice == "1":
        print(f"Your total points were {points}, Restarting game from beginning")
        points = 0
        main()
    else:
        print(f"Thank you for playing Kris Jordan dating sim, your total points were {points}")


if __name__ == "__main__":
    main()