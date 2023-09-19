import textwrap

from mini_games.simple_classics import guess_the_number
from mini_games.simple_classics import rock_paper_scissors


def main():
    menu: str = textwrap.dedent(
        """
        [0] Exit
        [1] Guess the Number Game
        [2] Rock, Paper, Scissors
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

            case _:
                print("Warning: Incorrect Input. Stopping Program...")
                return 0


if __name__ == "__main__":
    main()
