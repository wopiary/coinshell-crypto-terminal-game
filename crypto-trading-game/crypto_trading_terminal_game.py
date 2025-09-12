import os
import intro_message_animation_crypto_trading_terminal_game as intro_module
import h_command
import q_command
import time

def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    intro_module.introanimate(delay=0.03)
    
def commands():
    while True:
        intro()
        user_command = input("""

    (q) Quick Start
                             
    (h) Help
                             
    (e) Exit

    Enter command: """).strip().lower()

        if user_command == 'q':
            result = q_command.main()
        elif user_command == 'h':
            result = h_command.show_help()   
        elif user_command == 'e':
            os.system('cls' if os.name=='nt' else 'clear')
            print("Exiting Coin$hell...")   
            break
        else:
            print("Invalid command. Try again.")

if __name__ == '__main__':
    intro()
    commands()

