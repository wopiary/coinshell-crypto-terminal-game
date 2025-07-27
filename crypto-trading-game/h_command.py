import os

def show_help():
    os.system('cls' if os.name == 'nt' else 'clear')

    help_info = """
Welcome to Coin$hell

As you might have observed, Coin$hell does not support other stuff, only on the VSCode terminal. 
I made this for the sole purpose of being easier to use.

Nothing really much to teach here, controls are not complicated. 
Just click/type, that's about it. Go on ahead and gambl— trade!
"""
    print(help_info)

    while True:
        back_command = input("(b) to go back >> ").strip().lower()
        if back_command == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            return 'back'
        else:
            print("Invalid input. Press 'b' to go back.")
