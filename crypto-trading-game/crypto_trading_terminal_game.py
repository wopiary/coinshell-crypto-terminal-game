import os
import intro_message_animation_crypto_trading_terminal_game as intro_module
import h_command
import q_command
import time

def intro():
    os.system('cls' if os.name == 'nt' else 'clear')

    frames = [
            intro_module.A,
            intro_module.B,
            intro_module.C,
            intro_module.D,
            intro_module.E,
            intro_module.F,
        ]
    
    delay = 0.09
    intro_module.introanimate(frames, delay)
    
def commands():
    while True:
        intro()
        user_command = input("""

    (q) Quick Start
                             
    (h) Help
                             
    (e) Exit

    Enter command: """).strip().lower()

        if user_command == 'q':
            result = q_command.game()

        elif user_command == 'h':
            result = h_command.show_help()  # show help and wait for user to go back
            

        elif user_command == 'e':
            print("Exiting Coin$hell...")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == '__main__':
    intro()
    commands()
