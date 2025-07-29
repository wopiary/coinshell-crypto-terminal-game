import os
import time
import sys
import bytebucks
import random
def coin_selection():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)
    print("""
            Start your trading journey!
            Choose coin to purchase...
                                                                                            
""")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    coins_prices = [random.uniform(1.0, 1500.0) for _ in range(5)]
    print(f"""

                                                                                    Available Coins:
          
                                                                               (1) ByteBucks(BYB)  ==  ${coins_prices[0]: .5f}

                                                                               (2) LunaMint(LMT)   ==  ${coins_prices[1]: .5f}

                                                                               (3) Vironix(VRX)    ==  ${coins_prices[2]: .5f}

                                                                               (4) HexaFuel(HXF)   ==  ${coins_prices[3]: .5f}

                                                                               (5) OpalX(OPX)      ==  ${coins_prices[4]: .5f}

                                                    """)
    while True:
        user_coin_choice = input("""
                                                                            Selection one coin, enter number to buy>> """)
     
        
        if user_coin_choice == '1':
                print('ByteBucks Purchased')
        elif user_coin_choice == '2':
                print('LunaMint Purchased')
        elif user_coin_choice == '3':
                print('Vironix Purchased')
        elif user_coin_choice == '2':
                print('HexaFuel Purchased')
        elif user_coin_choice == '2':
                print('OpalX Purchased')
        else:
                    print("Selected Coin is Unavailable!")
         


def starting_message():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
=====================================================================================================================================================================================================================
=====================================================================================================================================================================================================================
                                                        __        __   _                            _           ____      _        _  _          _ _ 
                                                        \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___    / ___|___ (_)_ __  | || |__   ___| | |
                                                         \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |   / _ \| | '_ \ / __) '_ \ / _ \ | |
                                                          \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |__| (_) | | | | \__ \ | | |  __/ | |
                                                           \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \____\___/|_|_| |_|___/_| |_|\___|_|_|
=====================================================================================================================================================================================================================
=====================================================================================================================================================================================================================
          """)
    time.sleep(0.2)
    print("""       
                                                                          Ready to dive into the wild world of crypto trading?
                                                                                    Here's what you need to know:

                                                                                    💵 Starting Balance: $10,000
                                                                                   💹 Market is LIVE and volatile
                                                                                  ⌚ Every second counts in crypto!

                                                                       Trade smart, trade fast, and may the profits be with you!"""
    )
        
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
        starting_message()
        print("Loading market data...")
    
        spinner = '-\\|/'
        for i in range(100):  # your actual loop
        # your code here
                time.sleep(0.1)  # simulate work
                
                # Progress line - just add this:
                print(f'\r{spinner[i % 4]} Processing... {i+1}%', end='')
    
        print("\n\nMarket loaded! Let's start gambl- trading I mean!")
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
                choice = input("""

        (v) 📊 To view portfolio |                          

""")
