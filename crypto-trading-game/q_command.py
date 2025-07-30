import os
import time
import sys
import random
import threading
import fake_news
import line_graph
        


def coin_selection():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    coin_names = ['ByteBucks(BYB)', 'LunaMint(LMT)', 'Vironix(VRX)', 'HexaFuel(HXF)', 'OpalX(OPX)']
    coins_prices = [random.uniform(1.0, 1500.0) for _ in range(5)]
    
    print(f"""

                     Current Coin Prices:
          
 (1) {coin_names[0]}   ||   ${coins_prices[0]: .5f}
 (2) {coin_names[1]}   ||   ${coins_prices[1]: .5f}
 (3) {coin_names[2]}   ||   ${coins_prices[2]: .5f}
 (4) {coin_names[3]}   ||   ${coins_prices[3]: .5f}
 (5) {coin_names[4]}   ||   ${coins_prices[4]: .5f}
   """)
    while True:
        user_coin_choice = input("Selection one coin, enter number to buy >> ")
     
        
        if user_coin_choice == '1':
                
                print('ByteBucks Purchased')
                time.sleep(0.8)
                coin_selection()
        elif user_coin_choice == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('LunaMint Purchased')
        elif user_coin_choice == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Vironix Purchased')
        elif user_coin_choice == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('HexaFuel Purchased')
        elif user_coin_choice == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('OpalX Purchased')
        else:
                print("Selected Coin is Unavailable!")
        


def starting_message():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""

                                                        __        __   _                            _           ____      _        _  _          _ _ 
                                                        \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___    / ___|___ (_)_ __  | || |__   ___| | |
                                                         \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |   / _ \| | '_ \ / __) '_ \ / _ \ | |
                                                          \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |__| (_) | | | | \__ \ | | |  __/ | |
                                                           \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \____\___/|_|_| |_|___/_| |_|\___|_|_|

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
        
    
    print("Loading market data...")
    
    spinner = '-\\|/'
    for i in range(100): #CHANGE THIS SHIT BACK TO 100
                time.sleep(0.1)  
                
                
                print(f'\r{spinner[i % 4]} Processing... {i+1}%', end='')
    print("\n\nMarket loaded! Let's start gambl- trading I mean!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')




def game():
        
        starting_message()
        
        user_balance = 5000
        
        while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print('• Market is OPEN!\n')
                line_graph.line_graphs()

                print(f'💰 Wallet Balance: {user_balance}')
                fake_news.fake_news()
        
                        


                user_dashboard_choice = input("""\n(v) 📊 View portfolio  |  (m) 📈 View market  |  (r) 🪙 Purchase/sell coins  |  (e) 🚪 Exit                       
""").strip().lower()
                if user_dashboard_choice == 'v':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('portfolio logic')
                elif user_dashboard_choice == 'm':
                        print('market logic')
                elif user_dashboard_choice == 'r':
                        coin_selection()
                elif user_dashboard_choice == 'e':
                        break
                else:
                        print('Command Unavailable')
