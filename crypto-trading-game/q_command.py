import os
import time
import sys
import random
import threading
import fake_news
import line_graph


#GLOBAL
user_wallet = {
       'balance': 5000.00000
}
Name = None



#QUICKSCENE, THORNE NTRODUCES HIMSELF TO THE PLAYER AND ASK FOR NAME
def quick_scene(text, delay):
    os.system('cls' if os.name=='nt' else 'clear')
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()
# ceo_message = """
#            ⢀⠤⠐⠲⣦⠀⠀⠀⠐⡍⠥⠂⠀⠀⠀ Thorne:   ⠀⠀⠀⠀⠀              Alright, listen up. The name's Thorne. CEO of this whole damn operation. You're stepping into the arena now, kid,
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣦⡀⠠⠛⣧⡀⣀⠐⢑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀                       and in this game of crypto, where fortunes are made and lost faster than a blink, you gotta know who's on your side.
# ⠀⠀⠀⠀⢀⡄⠀⠀⠈⠣⡻⣿⠦⠐⠒⠚⠉⠣⠀⠀⠁⢕⢄⠀⠀⠀⠀⠀⠀⠀                       More importantly, you gotta know who you're dealing with. Every transaction, every trade, every whisper of a coin's 
# ⠀⡠⡔⠒⠃⢣⢀⣀⠀⢠⢊⠆⠁⠀⠀⠀⢀⠀⠁⠀⠀⠀⠊⡘⠀⠀⠀⠀⠀⠀                       rise or fall... it all comes down to trust. Or the lack thereof.
# ⢆⠠⠤⠀⠠⣦⣿⣿⣿⣾⣾⣁⡀⣀⡠⠀⢈⣈⡉⠃⠀⢠⡢⣚⡮⢖⢄⠀⠀⠀                       So, before we dive headfirst into this digital gold rush, let's get one thing straight.
# ⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⡮⠔⣂⠡⣬⣤⣤⣴⣿⣿⣾⠁⠀⠙⢕⣄⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠓⠀⢊⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠁⠵                        """ delete the following ceo_message, replace with this after you done
ceo_message = """
           test
        """



def users_name_info():
    global Name
    user_name = input("""       
                                                      What's your name, hotshot? """).strip().capitalize()
    Name = user_name
    return Name



def coins_page():
    global user_wallet
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    coin_names = ['|🦌| ByteBucks(BYB)', '|🌙| LunaMint(LMT)', '|🦠| Vironix(VRX)', '|⛽| HexaFuel(HXF)', '|❌| OpalX(OPX)', '|🌱| TerraGreen(TGR)', '|💡| Lumina(LMN)', '|⚙️| GearCoin(GRC)', '|🪐| Cosmic(CSC)', '|⚡️| VoltFlux(VFX)', '|🧬| GeneX(GNX)', '|🔮| Oracle(ORC)', '|🔑| KeyStone(KST)', '|🧊| CryoChain(CRC)']
    coin_prices = [random.uniform(1.0, 1500.0) for _ in range(14)]
    
    print(f""" 
        • GLOBAL MARKET 
|TICKET|       |COIN|              |VALUE|          
 (1)    {coin_names[0]}   ||   ${coin_prices[0]: .5f}             
 (2)    {coin_names[1]}    ||   ${coin_prices[1]: .5f}               
 (3)    {coin_names[2]}     ||   ${coin_prices[2]: .5f}              
 (4)    {coin_names[3]}    ||   ${coin_prices[3]: .5f}             
 (5)    {coin_names[4]}       ||   ${coin_prices[4]: .5f}            
 (6)    {coin_names[5]}  ||   ${coin_prices[5]: .5f}             
 (7)    {coin_names[6]}      ||   ${coin_prices[6]: .5f}            
 (8)    {coin_names[7]}     ||   ${coin_prices[7]: .5f} 
 (9)    {coin_names[8]}      ||   ${coin_prices[8]: .5f}
 (10)   {coin_names[9]}    ||   ${coin_prices[9]: .5f}
 (11)   {coin_names[10]}       ||   ${coin_prices[10]: .5f}
 (12)   {coin_names[11]}      ||   ${coin_prices[11]: .5f}
 (13)   {coin_names[12]}    ||   ${coin_prices[12]: .5f}
 (14)   {coin_names[13]}   ||   ${coin_prices[13]: .5f}

 press 6 to go back
   """)
    while True:
        chosen_coin_to_interact = input("Selection one coin, enter number to buy >> ")
     
        
        if chosen_coin_to_interact == '1':
                user_wallet['balance'] -= coin_prices[0]
                print('ByteBucks Purchased')
                print(f"New Balance: ${user_wallet['balance']:.2f}")
                time.sleep(0.8)

        elif chosen_coin_to_interact == '2':
                print('LunaMint Purchased')

        elif chosen_coin_to_interact == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Vironix Purchased')
        elif chosen_coin_to_interact == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('HexaFuel Purchased')
        elif chosen_coin_to_interact == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('OpalX Purchased')
        elif chosen_coin_to_interact == '6':
               print('TerraGreen Purchased')
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

                                                                                    💵 Starting Balance: $5,000
                                                                                   💹 Market is LIVE and volatile
                                                                                  ⌚ Every second counts in crypto!

                                                                       Trade smart, trade fast, and may the profits be with you!"""
    )
    time.sleep(2)
    quick_scene(ceo_message, delay=0.01)
    time.sleep(1)
    Name = users_name_info()
    time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Loading market data...")
    spinner = '-\\|/'
    for i in range(3): #CHANGE THIS SHIT BACK TO 100
                time.sleep(0.1)  
                
                
                print(f'\r{spinner[i % 4]} Processing... {i+1}%', end='')
    print("\n\nMarket loaded! Let's start gambl- trading I mean!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')




def main():
        starting_message()
        while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print('• Market is OPEN!\n')
                line_graph.line_graphs()
                print(f'\n👤: {Name}')
                print(f'💰 Wallet Balance: {user_wallet['balance']}')
                fake_news.fake_news()
        
                        


                user_dashboard_choice = input("""\n(v) 📊 View portfolio  |  (m) 📈 View market  |  (r) 🪙 Purchase/sell coins  |  (e) 🚪 Exit                       
""").strip().lower()
                if user_dashboard_choice == 'v':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('portfolio logic')
                elif user_dashboard_choice == 'm':
                        print('market logic')
                elif user_dashboard_choice == 'r':
                        coins_page()
                elif user_dashboard_choice == 'e':
                        break
                else:
                        print('Command Unavailable')
