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
