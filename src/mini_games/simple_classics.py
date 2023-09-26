import random, textwrap



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

    categories = {
        "geography": [
            {"question": "What is the capital of Japan?", "answer": ["tokyo"]},
            {"question": "Which country is the Kremlin located in?", "answer": ["russia"]},
            {"question": "How many states does the USA have?", "answer": ["50"]},
            {"question": "What is the dominant language of Belgium?", "answer": ["french"]},
            {"question": "What is the country to the south of Mt. Everest?", "answer": ["nepal"]},
            {"question": "What is the capital of Brazil?", "answer": ["brasilia"]},
            {"question": "Which lake does the Nile come from?", "answer": ["victoria"]},
            {"question": "Which country has a flag featuring a purple parrot in it?", "answer": ["dominica"]},
            {"question": "Spell the capital of Burkina Faso correctly.", "answer": ["ouagadougou"]},
            {"question": "Which country uses long white license plates with blue text, featuring a Mokorotlo in it?", "answer": ["lesotho"]},
        ],
        "history": [
            {"question": "What country was ruled by Pharaohs?", "answer": ["egypt"]},
            {"question": "What is the oldest known civilization?", "answer": ["sumer"]},
            {"question": "Which river is the birthplace of Chinese civilization?", "answer": ["yellow"]},
            {"question": "What were the feudal lords of the Samurai called?", "answer": ["daimyo"]},
            {"question": "What was the lingua franca of the Aztecs?", "answer": ["nahuatl"]},
            {"question": "What was the period of warring states called in Japan?", "answer": ["sengoku jidai"]},
            {"question": "What were Roman baths called?", "answer": ["thermae"]},
            {"question": "Which Zulu king led the Zulus in the Anglo-Zulu war?", "answer": ["cetshwayo"]},
            {"question": "What year was Benito Mussolini's March on Rome?", "answer": ["1922"]},
            {"question": "Which Yuan dynasty leader launched a naval expedition to punish Kertanegara?", "answer": ["kublai khan"]},
        ],
        "anime": [
            {"question": "What is Goku's signature technique?", "answer": ["kamehameha"]},
            {"question": "What famous jutsu in Naruto takes the form of a spinning ball of chakra?", "answer": ["rasengan"]},
            {"question": "Which dere archetype is known for showing love and obsession to the point of being dangerously possessive and violent?", "answer": ["yandere"]},
            {"question": "What is Izuku Midoriya's hero name?", "answer": ["deku"]},
            {"question": "What type of magic is used by Megumin?", "answer": ["explosion"]},
            {"question": "What stand does Jotaro Kujo use?", "answer": ["star platinum"]},
            {"question": "What great tomb is the headquarters of Ainz Ooal Gown?", "answer": ["nazarick"]},
            {"question": "Which anime studio animated the first season of One-Punch Man?", "answer": ["mad house"]},
            {"question": "Which dere archetype is used to describe someone with a God-complex?", "answer": ["kamidere"]},
            {"question": "Which is the one Danganronpa character that loves Bojobo dolls?", "answer": ["Kyoko Kirigiri"]},
        ]
    }

    def category(category_name, questions):
        score = 0

        print(f"{category_name} quiz")

        for real_question in questions:
            question = real_question["question"]
            answers = real_question["answer"]

            print(f"{question}")
            player_answer = input().lower()

            if player_answer in answers:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {answers}")


        print(f"You got {score} out of {len(questions)} questions correct in {category_name} quiz.")

    while True:

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
                    print("Loading back menu . . .")
                    return 0
                case "1":
                    category("geography", categories["geography"])
                case "2":
                    category("history", categories["history"])
                case "3":
                    category("anime", categories["anime"])
                case _:
                    print("Warning: Incorrect Input. Stopping Program...")
                    return 0




