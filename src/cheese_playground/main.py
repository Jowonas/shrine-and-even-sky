import textwrap

from src.cheese_playground.mini_games.simple_classics import guess_the_number, rock_paper_scissors, quiz_game


def main():
    menu: str = textwrap.dedent(
        """
        [0] Exit
        [1] Guess the Number Game
        [2] Rock, Paper, Scissors
        [3] Quiz Game
        Enter one of the above choices to continue: 
        """
    )

    while True:
        picked_action = input(menu)

        match picked_action:
            case "0":
                print("Stopping Program...")
                return 0
            case "1":
                guess_the_number()
            case "2":
                rock_paper_scissors()
            case "3":
                quiz_game()
            case _:
                print("Warning: Incorrect Input. Stopping Program...")
                return 1


if __name__ == "__main__":
    main()
