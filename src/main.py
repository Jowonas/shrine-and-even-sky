def main():
    import random
    seggs = (random.randint(1, 100))
    guess = int(input("Gib me ur guess 1-100"))

    while guess != seggs:

        if guess < seggs:

            print("ur lower")
        elif guess > seggs:

            print("ur higher")
        guess = int(input("Gib me ur guess 1-100: "))

    print("damn right")

    #fsafafesf



if __name__ == "__main__":
    main()
