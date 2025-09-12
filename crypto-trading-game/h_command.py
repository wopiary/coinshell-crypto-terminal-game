import os

def show_help():
    os.system('cls' if os.name == 'nt' else 'clear')

    help_info = """
Welcome to Coin$hell!

This tool is made purely to be played on the VSCode terminal.
Here you get to experience and learn the basics of crypto trading.
Engage and explore the different features and act as a savy young adult
taking on the world of trading. There's not much to learn—simply type
the assigned the letter for each command.

Go on ahead and gambl— trade!
-@wopiary
"""
    print(help_info)

    while True:
        back_command = input("(b) to go back >> ").strip().lower()
        if back_command == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            return 'back'
        else:
            print("Invalid input. Press 'b' to go back.")
