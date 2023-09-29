def txt_file_writer() -> None:
    """This function writes userinput into a demofile"""

    user_input: str = input("Write down the message to append to the file: ")
    with open("demofile.txt", "a") as demo_file:
        demo_file.write(f"{user_input}\n")
