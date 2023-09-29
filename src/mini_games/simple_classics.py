import random
import textwrap
import json


def guess_the_number() -> None:
    """
    This function implements a typical guess the number game
    it uses a guess loop until the answer is correct
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
    """Rock Paper Scissors game following the normal rule set"""

    choices: list = ["rock", "paper", "scissors"]
    cpu_pick: str = random.choice(choices)
    player_pick: str = input("Pick between rock, paper, or scissors or press enter to cancel:")
    player_pick = player_pick.lower()

    if player_pick not in choices:
        print(f"That is not a valid pick, please make sure to pick one of the following next time: {choices}")

    if player_pick == cpu_pick:
        print(f"It's a tie")
    elif player_pick == 'rock' and cpu_pick == 'scissors':
        print(f"You beat me. I picked {cpu_pick}")
    elif player_pick == 'paper' and cpu_pick == 'rock':
        print(f"You beat me. I picked {cpu_pick}")
    elif player_pick == 'scissors' and cpu_pick == 'paper':
        print(f"You beat me. I picked {cpu_pick}")
    else:
        print(f"You have lost. I picked {cpu_pick}")


def quiz_game() -> None:
    """"Quiz game with 3 categories"""

    def __category(category_name):
        # load the categories out of the json file #
        with open("mini_games/categories.json") as c_file:
            categories: list = json.load(c_file)
        for category in categories:
            # check if category exists#
            if category.get("name") == category_name:
                questions_answers = category["questions_answers"]
                score = 0

                print(f"{category_name} quiz:\n")

                for q_a in questions_answers:
                    question = q_a["question"]
                    answer = q_a["answer"]

                    print(f"{question}")
                    player_answer = input().lower()

                    if player_answer == answer:
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is: {answer}")

                print(f"You got {score} out of {len(questions_answers)} questions correct in {category_name} quiz.")

    menu: str = textwrap.dedent(
        """
        [0] Exit
        [1] Geography
        [2] History
        [3] Anime
        Pick a category to play: 
        """
    )

    while True:
        picked_action = input(menu)

        match picked_action:
            case "0":
                print("Loading back menu...")
                break
            case "1":
                __category("geography")
            case "2":
                __category("history")
            case "3":
                __category("anime")
            case _:
                print("Warning: Incorrect Input. Loading back menu...")
                break
