def main():
    import random
    seggs = (random.randint(1, 100))
    guess = int(input("Gib me ur guess 1-100"))
    if seggs==guess:
        print("damn right")
    elif guess < seggs:
        print("ur lower")
    elif guess > seggs:
        print("ur higher")






    print(seggs)
    #fsafafesf



if __name__ == "__main__":
    main()
