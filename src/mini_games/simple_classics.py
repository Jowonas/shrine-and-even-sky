import random


def guess_the_number() -> None:
    """
    This function implements a typical guess the number game
    it uses a guess loop until the answer is correct

    :return: None
    """
    picked_number: int = random.randint(1, 100)
    guessed_number: int | None = None

    default_error: str = "Your Input was not a valid number"

    while guessed_number != picked_number:
        guess = input("Give a number between 1-100 or press enter to cancel: ")

        # Allow the user to exit the game
        if guess is None:
            print(f"The Number was {picked_number}, cancelling game...")
            return

        # Invalid Input Handling
        else:
            try:
                guessed_number = int(guess)
            except ValueError:
                print(default_error)
        if guessed_number not in range(1, 101):
            print(default_error)

        # Value Comparison
        if guessed_number > picked_number:
            print("your guess is too large")
        elif guessed_number < picked_number:
            print("your guess is too small")

    print(f"Congrats, you picked the correct number {picked_number}")

def rock_paper_scissors() -> None:

    janken_choices = ["rock","paper","scissors"]
    cpu_pick = (random.choice(janken_choices))

    player_pick = input("Pick between rock, paper, or scissors or press enter to cancel:")

    if player_pick == cpu_pick:
        print(f"It's a tie")

    elif (player_pick == 'rock' and cpu_pick == 'scissors'):
        print (f"You beat me. I picked {cpu_pick}")

    elif (player_pick == 'paper' and cpu_pick == 'rock'):
        print (f"You beat me. I picked {cpu_pick}")

    elif (player_pick == 'scissors' and cpu_pick == 'paper'):
        print (f"You beat me. I picked {cpu_pick}")

    else:
        print(f"You're a failure. I picked {cpu_pick}")

