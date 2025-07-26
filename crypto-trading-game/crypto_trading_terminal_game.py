import time
import sys
import intro_message_animation_crypto_trading_terminal_game
import os
# def welcomemessage(text, delay):
#     for character in text:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()
# message = "CRYPTO Tradeing"
# welcomemessage(message, delay=0.04)

# WELCOME MESSAGE HERE

def commands():
    import intro_message_animation_crypto_trading_terminal_game

    user_command = input("""
        
        
    (q) Quick Start
                  
    (h) Help           
            
    (e) Exit
                    
                                
    Enter command:  """)
    if user_command == 'q':
        print('q command')
    elif user_command == 'h':
        import h_command
    # elif user_command == 'e':
        

commands()

