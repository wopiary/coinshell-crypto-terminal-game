import os

os.system('cls' if os.name =='nt' else 'clear')

help_info = """
Welcome to Coin$hell

As you might have observed, Coin$hell does not support other shit, only on the VSCode terminal. 
I made this for the sole purpose of being easier to use.

Nothing really much to teach here, controls are not complicated. 
Just click/type, thats about it. Go on ahead and gambl- trade!

"""

for _ in range(1):
    print(help_info)

back_command = input('(b) to go back >> ')

if back_command == 'b':
    os.system('cls' if os.name =='nt' else 'clear')
    # Import and call the main file's commands function

    import crypto_trading_terminal_game
    crypto_trading_terminal_game.commands()