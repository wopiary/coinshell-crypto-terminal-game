import os
import time
import sys
import random
import threading
import fake_news
import line_graph
import string
from datetime import datetime

#GLOBAL
user_wallet = {
       'balance': 999999.00
}
Name = None
# coin_prices = [random.uniform(1.0, 1000.0) for _ in range(14)]
bag = {
      'coins_owned': []
}
black_market_page_product_category = [
    "Crypto Exchange",
    "Compromised Coinshell Accounts",
    "Misc. Black Market Goods",
    "Exit Silk Claw"
]
bag_black_market = {
      'crypto_coin' : []
}


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
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠓⠀⢊⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠁⠵                        """ #delete the following ceo_message, replace with this after you done
ceo_message = """
           yr
        """






def users_name_info():
    global Name
    user_name = input("""       
                                                      What's your name, hotshot? """).strip().capitalize()
    Name = user_name
    return Name

def coin_purchase_prices_updates(): 
      global coin_prices_low_range, coin_prices_mid_range, coin_prices_high_range
      coin_prices_low_range = [random.uniform(0.01, 5.0) for _ in range(3)]
      coin_prices_mid_range = [random.uniform(10, 500) for _ in range(4)]
      coin_prices_high_range = [random.uniform(1001,70000) for _ in range(3)]
      
coin_purchase_prices_updates()

def coins_sell_prices_updates():
     global coin_sell_prices_low_range, coin_sell_prices_mid_range, coin_sell_prices_high_range
     coin_sell_prices_low_range = [round(random.uniform(0.005, 4.8000), 4) for _ in range(3)]
     coin_sell_prices_mid_range = [round(random.uniform(8.5000, 480.0000), 4) for _ in range(4)]
     coin_sell_prices_high_range = [round(random.uniform(950.0000, 68000.0000), 4) for _ in range(3)]
     
coins_sell_prices_updates()


# 'B' COMMAND

def black_market_page_generate_key(length =6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def black_market_page():
    os.system('cls' if os.name == 'nt' else 'clear')
    global session_code_first_num, session_code_letters, session_code_second_num, sections
    
    
#     # # Spooky loading effect
    # print("    🌐 Initiating secure connection to darknet terminal...")
    # time.sleep(2)
    # os.system('cls' if os.name == 'nt' else 'clear') 
    # print("    🔐 Authenticating user credentials...")
    # time.sleep(2)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print("    👁️  Synchronizing with decentralized nodes...")
    # time.sleep(1.5)
    # os.system('cls' if os.name == 'nt' else 'clear')

    # print("    ⚡ Connection established. Welcome to the Market!")
    # time.sleep(2)
    # os.system('cls' if os.name == 'nt' else 'clear')


    session_code_first_num = random.randint(1,9)
    session_code_second_num = random.randint(10,99)
    session_code_letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    account_num = random.randint(1000,9999)

    access_keys = {black_market_page_generate_key(): category for category in black_market_page_product_category}

    print(f"""
⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢠⢤⣠⣶⣿⣿⡿⠿⠛⠛⠛⠛⠉⠛⠛⠛⠛⠿⣷⡦⠞⣩⣶⣸⡆⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⣠⣾⡤⣌⠙⠻⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠋⢀⣾⣿⣿⠃⣇⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣠⣾⣿⡟⢇⢻⣧⠄⠀⠈⢓⡢⠴⠒⠒⠒⠒⡲⠚⠁⠀⠐⣪⣿⣿⡿⡄⣿⣷⡄⠀⠀⠀⠀⠀
            ⠀⠀⠀⣠⣿⣿⠟⠁⠸⡼⣿⡂⠀⠀⠈⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠉⠹⣿⣧⢳⡏⠹⣷⡄⠀⠀⠀⠀
            ⠀⠀⣰⣿⡿⠃⠀⠀⠀⢧⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠇⡸⠀⠀⠘⢿⣦⣄⠀⠀
            ⠀⢰⣿⣿⠃⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠀⠀⠀⠀⠀⠀⠰⡇⠀⠀⠀⠈⣿⣿⣆⠀
            ⠀⣿⣿⡇⠀⠀⠀⠀⢰⠇⠀⢺⡇⣄⠀⠀⠀⠀⣤⣶⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠸⣿⣿⡀
            ⢸⣿⣿⠀⠀⠀⠀⠀⢽⠀⢀⡈⠉⢁⣀⣀⠀⠀⠀⠉⣉⠁⠀⠀⠀⣀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⣿⣿⡇
            ⢸⣿⡟⠀⠀⠀⠠⠀⠈⢧⡀⠀⠀⠀⠹⠁⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⢼⠁⠀⠀⠀⠀⠀⢹⣿⡇
            ⢸⣿⣿⠀⠀⠀⠀⠀⠠⠀⠙⢦⣀⠠⠊⠉⠂⠄⠀⠀⠀⠈⠀⠀⠀⣀⣤⣤⡾⠘⡆⠀⠀⠀⠀⠀⣾⣿⡇
            ⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⢠⠜⠳⣤⡀⠀⠀⣀⣤⡤⣶⣾⣿⣿⣿⠟⠁⠀⠀⡸⢦⣄⠀⠀⢀⣿⣿⠇
            ⠀⢿⣿⣧⠀⠀⠀⠀⠀⣠⣤⠞⠀⠀⠀⠙⠁⠙⠉⠀⠀⠸⣛⡿⠉⠀⠀⠀⢀⡜⠀⠀⠈⠙⠢⣼⣿⡿⠀
            ⠀⠈⣿⣿⣆⠀⠀⢰⠋⠡⡇⠀⡀⣀⣤⢢⣤⣤⣀⠀⠀⣾⠟⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⣰⣿⣿⠁⠀
      ⠀⠀⠀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     ████  SILK CLAW MARKETPLACE v3.1  ████   [SECURE NODE: ACTIVE]
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      Session: #{session_code_letters}{session_code_first_num}-{session_code_second_num} │ Encrypted Route: ONION://v3
      Account: ANON-{account_num} │ Clearance Level: OMEGA | Inventory: {bag_black_market['crypto_coin']}
──────────────────────────────────────────────────────────────────────
      """)
    
    for key, section in access_keys.items():
      print(f"?  {key}   – {section}")

    black_market_page_choice = input("""
Enter Access Key to Proceed:
""")
    
    if black_market_page_choice in access_keys:
        section = access_keys[black_market_page_choice]
        print(f"\n[ACCESS GRANTED] Redirecting to {section}...\n")

    if section == 'Crypto Exchange':
        black_market_page_crypto_coin()

    elif section =='Exit Silk Claw':
         return 'back'
        
    else:
        print("\n[ACCESS DENIED] Invalid key. Disconnecting...\n")
        return black_market_page()




def black_market_page_crypto_coin():

            os.system('cls' if os.name=='nt' else 'clear')
            global  bm_crypto_exchange_page_coin_prices
            bm_crypto_exchange_page_coin_names = [
            "🕱 Shadowcoin (SHC)",
            "⚓ Dreadnaught (DNT)",
            "🐍 Chimera (CMR)",
            "✴ Aetherium (AET)",
            "🌑 Aphelion (APH)"
        ]
            bm_crypto_exchange_page_coin_prices = [random.uniform(5000,99999) for _ in range(6)]
            bm_crypto_exchange_page_coin_value = [random.uniform(-99999,99999) for _ in range(6)]
            print(f"""

        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⢀⣠⣶⣿⡟
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠉⠙⠛⠛⠛⠿⠋⠀⣀⣴⣿⣿⣿⠋⣰
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⡀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡏⣩⣤⠄⣠⣶⣶⡶⢀⣤⡀⠀⣠⣾⣿⣿⣿⡿⢃⣼⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣿⢃⣾⣿⣿⢋⣴⣿⠟⣠⣿⣿⣿⣿⣿⣿⠁⠾⠿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⢃⣾⣿⣿⢃⣾⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣴⠋⣠⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠉⠀⣠⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣦⣠⣾⣿⣿⣧⡘⠿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⣿
        ⣿⣿⣿⣿⣿⡟⠁⠀⠈⠉⠛⠏⠀⣴⣤⣴⣿⣿⣿⡿⠋⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌
        ⣿⣿⡿⠋⠉⠁⢀⣿⡃⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢸⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠁⠀⠉⠙⢿⣿⣿⣿⣿⣿
        ⣿⠋⠀⣠⣶⣷⣾⣿⣿⣿⣄⠲⣤⣀⠀⠈⠙⠿⣿⡀⠀⠀⠀⣠⡞⣩⣴⣾⣿⣿⣿⣶⣬⣛⢿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿
        ⡇⠀⣴⣿⡿⠉⠉⠉⠻⣿⣿⣇⠠⢉⠻⢦⣄⠀⠈⠻⢷⣶⣿⡏⣾⡀⠿⣿⡿⠻⣿⣿⣿⠛⣧⡹⣿⣇⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿
        ⡇⠀⣿⣿⠀⠀⠀⠀⠀⢻⣿⡿⢸⣷⣬⡂⢍⠻⢶⣄⡀⠉⠛⢷⣿⣷⣦⣤⣴⣦⣈⣉⣁⣠⣾⡇⣿⣿⣦⣀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿
        ⡇⠀⣿⣿⣆⠀⠀⠀⣠⣿⣿⣧⢸⣿⣿⣿⣷⣬⣐⣬⡙⠢⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⡇⠀⣿⣿⣿⣿⠿⢿⡿⠿⠿⠟⢼⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⣷⠀⡄⠀⠈⠛⠛⠛⠛⠿⠿⣫⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⡇⠀⣿⡛⢹⣇⠀⣠⡏⢘⣿⣿⣶⣌⠙⠻⢿⣿⣿⣿⣿⣿⠀⣿⠀⡇⢰⡆⣄⠀⠀⢤⡀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⡇⠀⢻⣷⣤⣙⣛⣋⣴⣿⠿⠟⣿⣿⢸⠀⡆⢈⢙⠻⢿⣿⠀⠿⠀⣿⢸⡇⣿⠀⣆⢠⣈⠃⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣇⠀⠀⢉⠛⠛⠛⠛⠋⠁⠤⡀⠈⠙⠘⠆⡇⢸⠈⣷⣦⣍⡀⠄⡀⠉⠈⠃⢿⠀⣿⢸⣭⣷⣦⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     ████  SILK CLAW MARKETPLACE v3.1  ████   [SECURE NODE: ACTIVE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CRYPTO EXCHANGE NODE] — SILK CLAW MARKETPLACE v3.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: ACTIVE │ Wallet Integration: ENABLED │ Escrow: SECURED
Wallet: ${user_wallet['balance']:.2f}        | Inventory: 
     {bag_black_market['crypto_coin']}
──────────────────────────────────────────────────────────────────────
 ID   │ ITEM/DESCRIPTION                  │ PURCHASE VALUE
──────┼───────────────────────────────────┼───────────────────────────
 001  │ 🕱 Shadowcoin (SHC)                │ ${bm_crypto_exchange_page_coin_prices[0]:.2f}
 002  │ ⚓ Dreadnaught (DNT)              │ ${bm_crypto_exchange_page_coin_prices[1]:.2f}
 003  │ 🐍 Chimera (CMR)                  │ ${bm_crypto_exchange_page_coin_prices[2]:.2f}
 004  │ ✴ Aetherium (AET)                 │ ${bm_crypto_exchange_page_coin_prices[3]:.2f}
 005  │ 🌑 Aphelion (APH)                 │ ${bm_crypto_exchange_page_coin_prices[4]:.2f}
──────────────────────────────────────────────────────────────────────
[1] Purchase Coin
[2] Dump Coin
[3] Return to Access Gate """)  
            print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
            black_market_page_crypto_coin_user_input = input('Enter your choice: ')

            if black_market_page_crypto_coin_user_input == '1':
                 os.system('cls' if os.name == 'nt' else 'clear') 
                #  print("    🔗 Initiating encrypted uplink to the terminal nexus...")
                #  time.sleep(1.5)
                #  print("    🔐 Validating PGP keys and executing secure handshake...")
                #  time.sleep(1.5)
                #  print("    🔄 Synchronizing transaction logs and validating cipher chains...")
                #  time.sleep(1.5)
                #  os.system('cls' if os.name == 'nt' else 'clear') 
                #  print("    🟢 Connection established. Market is online. Stay anonymous.")
                #  time.sleep(2)
                
                 black_market_page_crypto_coin_purchase_coin_page()
            
def black_market_page_crypto_coin_purchase_coin_page():
            os.system('cls' if os.name=='nt' else 'clear')
            tx_hash = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CRYPTO EXCHANGE || PURCHASE NODE] — SILK CLAW MARKETPLACE v3.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: ACTIVE │ Wallet Integration: ENABLED │ Escrow: SECURED
Wallet: ${user_wallet['balance']:.2f}        | Inventory: {bag_black_market['crypto_coin']}
──────────────────────────────────────────────────────────────────────
 ID   │ ITEM/DESCRIPTION                  │ PURCHASE VALUE
──────┼───────────────────────────────────┼───────────────────────────
 001  │ 🕱 Shadowcoin (SHC)                │ ${bm_crypto_exchange_page_coin_prices[0]:.2f}
 002  │ ⚓ Dreadnaught (DNT)              │ ${bm_crypto_exchange_page_coin_prices[1]:.2f}
 003  │ 🐍 Chimera (CMR)                  │ ${bm_crypto_exchange_page_coin_prices[2]:.2f}
 004  │ ✴ Aetherium (AET)                 │ ${bm_crypto_exchange_page_coin_prices[3]:.2f}
 005  │ 🌑 Aphelion (APH)                 │ ${bm_crypto_exchange_page_coin_prices[4]:.2f}
──────────────────────────────────────────────────────────────────────
""")


            print("""
██████████████████████████████████████████████████████████████████████
█                                                                    █
█  ⬛ SILK CLAW SECURE TRANSACTION PROTOCOL ⬛                       █
█                                                                    █  
█  [ENCRYPTED] TOR://v3.onion/secure-payment                         █
█  [STATUS] AUTHENTICATED | ESCROW ENABLED | SSL 256-BIT             █
████████████████████████████████████████████████████████████████████ █
█                                                                    █
█  ⚠️  ENTER TRANSACTION DETAILS - ALL DATA IS ENCRYPTED  ⚠️          █
█                                                                    █
██████████████████████████████████████████████████████████████████████
""")
            black_market_page_crypto_coin_purchase_coin_page_receipt_coinname = input('[INPUT] ⬛ TARGET ASSET ID: ')
            if len(black_market_page_crypto_coin_purchase_coin_page_receipt_coinname.strip()) == 0:
                        black_market_page_crypto_coin_purchase_coin_page()
            black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity_input = input('[INPUT] 📦 QUANTITY UNITS: ')
            if len(black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity_input.strip()) == 0:
                         black_market_page_crypto_coin_purchase_coin_page()

            black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity = int(black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity_input)

            black_market_page_crypto_coin_purchase_coin_page_receipt_coinnconfirmation= input('[CONFIRM] ✅ AUTHORIZE TRANSACTION (Y/N): ')

            if black_market_page_crypto_coin_purchase_coin_page_receipt_coinnconfirmation == 'y':
                if black_market_page_crypto_coin_purchase_coin_page_receipt_coinname == '001':
                    total = bm_crypto_exchange_page_coin_prices[0] * black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased = '🕱 Shadowcoin (SHC)'
                elif black_market_page_crypto_coin_purchase_coin_page_receipt_coinname == '002':
                    total = bm_crypto_exchange_page_coin_prices[0] * black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased = '⚓ Dreadnaught (DNT)'
                elif black_market_page_crypto_coin_purchase_coin_page_receipt_coinname == '003':
                    total = bm_crypto_exchange_page_coin_prices[0] * black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased = '🐍 Chimera (CMR)'
                elif black_market_page_crypto_coin_purchase_coin_page_receipt_coinname == '004':
                    total = bm_crypto_exchange_page_coin_prices[0] * black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased = '✴ Aetherium (AET)'
                elif black_market_page_crypto_coin_purchase_coin_page_receipt_coinname == '005':
                    total = bm_crypto_exchange_page_coin_prices[0] * black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased = '🌑 Aphelion (APH)'
                else:
                    print('\n❌ Product Unavailable!')
                    time.sleep(2)
                    return  black_market_page_crypto_coin_purchase_coin_page()
                

                if user_wallet['balance'] >= total:
                    user_wallet['balance'] -= total
                    if 'crypto_coin' not in bag_black_market or not isinstance(bag_black_market['crypto_coin'], dict):
                        bag_black_market['crypto_coin'] = {}
                    
                    if black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased in bag_black_market['crypto_coin']:
                        bag_black_market['crypto_coin'][black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased] += black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    else:
                        bag_black_market['crypto_coin'][black_market_page_crypto_coin_purchase_coin_page_receipt_coinname_purchased] = black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity
                    # time.sleep(1)

                    # print("\n\n")
                    # print("    ➡️ Executing decentralized transaction. Awaiting block confirmation...")
                    # time.sleep(2)
                    # print("    ✅ Transaction hash generated and validated. Escrow release initiated...")
                    # time.sleep(3)
                    print(f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ████  SILK CLAW TRANSACTION RECEIPT  ████   [TX: CONFIRMED]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Session: {session_code_first_num}{session_code_letters}-{session_code_second_num} │ Hash: {tx_hash}
 Node: SECURE │ Protocol: ONION://v3 │ Status: COMPLETE
──────────────────────────────────────────────────────────────────────
 Operation: Crypto Exchange    │ Asset: {black_market_page_crypto_coin_purchase_coin_page_receipt_coinname}
 Quantity: {black_market_page_crypto_coin_purchase_coin_page_receipt_coinquantity:<13}       │ Value: ${total:.2f}
 Wallet Balance: ${user_wallet['balance']:.2f}       │ Escrow: RELEASED
──────────────────────────────────────────────────────────────────────
 [ENCRYPTED] ALL DATA ANONYMIZED │ TX IRREVERSIBLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
                else:
                    print('❌ Transaction failed: Insufficient funds!')
                    time.sleep(2)
                    return black_market_page_crypto_coin()
                time.sleep(2)
                return black_market_page_crypto_coin()
            elif black_market_page_crypto_coin_purchase_coin_page_receipt_coinnconfirmation == 'n':
                 print('❌ Transaction cancelled!')
                 time.sleep(2)
                 return black_market_page_crypto_coin()
            else:
                 print('❌ Command Unavailable!')
                 time.sleep(2)
                 return black_market_page()
                    

# 'R' COMMAND, BUYING AND SELLING

def coins_page():
    global user_wallet
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    coin_names = ['|🦌| ByteBucks(BYB)', '|🌙 | LunaMint(LMT)', '|🦠| Vironix(VRX)', '|⛽| HexaFuel(HXF)', '|❌| OpalX(OPX)', '|🌱| TerraGreen(TGR)', '|💡| Lumina(LMN)', '|⚙️| GearCoin(GRC)', '|🪐| Cosmic(CSC)', '|⚡️| VoltFlux(VFX)']
    marketcap_projection = random.uniform(1.0, 205.0)    
    tradingvol_projection = random.uniform(10., 999.0) 
    orders_of_magnitude = random.choice(['B', 'T'])



    print(f"""
    ╔═════════════════════════════════════════════════════════════════════════════════════════╗
    ║      🏛️  Coin$hell Trading                                                               ║
    ║      DIGITAL WEALTH MANAGEMENT SUITE                📈 Markets: OPEN                    ║
    ║      Institutional Trading Platform v12.4.1         🔒 Session: Encrypted               ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════╚
        ══════════════════════════════════════════════════════════════════════════════════
               Coin$hell LLC | Member FINRA/SIPC | FDIC Insured | SOX Compliant
           © 2025 Coin$hell & Co. All rights reserved. | Regulatory: SEC/CFTC Licensed
        ══════════════════════════════════════════════════════════════════════════════════
┌────────────────────────────┐     ┌────────────────────────────┐     ┌────────────────────────────┐
│   1. {coin_names[0]}   │     │  2. {coin_names[1]}    │     │  3. {coin_names[2]}      │
│                            │     |                            │     │                            │
│        $ {coin_prices_high_range[0]:.2f}                          $ {coin_prices_mid_range[1]:.2f}                          $ {coin_prices_mid_range[0]:.2f}            
│                            │     │                            │     │                            │
└────────────────────────────┘     └────────────────────────────┘     └────────────────────────────┘
┌────────────────────────────┐     ┌────────────────────────────┐     ┌────────────────────────────┐
│   4. {coin_names[3]}    │     │      5. {coin_names[4]}    │     |  6. {coin_names[5]}   │
│                            │     |                            │     │                            │
│        $ {coin_prices_high_range[1]:.2f}                           $ {coin_prices_high_range[2]:.2f}                        $ {coin_prices_low_range[1]:.2f}            
│                            │     │                            │     │                            │
└────────────────────────────┘     └────────────────────────────┘     └────────────────────────────┘
┌────────────────────────────┐     ┌────────────────────────────┐     ┌────────────────────────────┐
│     7. {coin_names[6]}    │     │    8. {coin_names[7]}    │     |  9. {coin_names[8]}       │
│                            │     |                            │     │                            │
│        $ {coin_prices_low_range[2]:.2f}                           $ {coin_prices_mid_range[3]:.2f}                        $ {coin_prices_mid_range[2]:.2f}            
│                            │     │                            │     │                            │
└────────────────────────────┘     └────────────────────────────┘     └────────────────────────────┘
┌────────────────────────────┐  
│    10. {coin_names[9]}  │  
│                            │  
│          $ {coin_prices_low_range[0]:.2f}          
│                            │   
└────────────────────────────┘  

\n💼 Portfolio Balance: ${user_wallet['balance']:.2f}   ||  🔒 Account Status: VERIFIED ✓
📊 Market Cap: ${marketcap_projection:.2f}{orders_of_magnitude}   ||  ⚡ Current Market Trading Volume: ${tradingvol_projection:.2f}
🎒 Inventory: {bag['coins_owned']}
""") 
    
    coins_page_dashboard_choice = input(
"""[b] 🟢 Buy     [s] 🔴 Sell     [e] 🚪 Return to Home
""") 
    print("""
┌─ INSTITUTIONAL SERVICES ───────────────────────────────────────────────────────┐
│ 📞 Private Banking: 1-800-CSH-PRIME │ 🌐 Research Portal: csh.com/research    │
│ 💬 Concierge: Available 24/7/365    │ 📧 Support: institutional@coinshell.com │
└────────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════
Coin$hell LLC | Member FINRA/SIPC | FDIC Insured | SOX Compliant
© 2025 Coin$hell & Co. All rights reserved. | Regulatory: SEC/CFTC Licensed
══════════════════════════════════════════════════════════════════════════════════""") 

    
    if coins_page_dashboard_choice == 'b':
               coins_page_buy_command()
            
    elif coins_page_dashboard_choice == 's':
               coins_page_sell_command()

    elif coins_page_dashboard_choice == 'e':
               return 'back'






def coins_page_buy_command():
    os.system('cls' if os.name=='nt' else 'clear')
    coin_names = ['|🦌| ByteBucks(BYB)', '|🌙| LunaMint(LMT)', '|🦠| Vironix(VRX)', '|⛽| HexaFuel(HXF)', '|❌| OpalX(OPX)', '|🌱| TerraGreen(TGR)', '|💡| Lumina(LMN)', '|⚙️| GearCoin(GRC)', '|🪐| Cosmic(CSC)', '|⚡️| VoltFlux(VFX)']

    print(f"""
██████████████████████████████████████████████████████████████████████████████
█ ░░░░░░░░░░░░░░░░░░░░░ OFFICIAL CRYPTO PURCHASE PORTAL ░░░░░░░░░░░░░░░░░░░░ █
██████████████████████████████████████████████████████████████████████████████
╠════════════════════════════════════════════════════════════════════════════╣
║                         📈 LIVE MARKET BOARD                               ║
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     #      ║ NAME                    ║ PRICE (USD)                         ║
╠════════════╬═════════════════════════╬═════════════════════════════════════╣
║     1      ║ {coin_names[0]}     ║ $ {coin_prices_high_range[0]:.2f}
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     2      ║ {coin_names[1]}      ║ $ {coin_prices_mid_range[1]:.2f}  
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     3      ║ {coin_names[2]}       ║ $ {coin_prices_mid_range[ 0]:.2f}     
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     4      ║ {coin_names[3]}      ║ $ {coin_prices_high_range[1]:.2f} 
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     5      ║ {coin_names[4]}         ║ $ {coin_prices_high_range[2]:.2f}   
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     6      ║ {coin_names[5]}    ║ $ {coin_prices_low_range[1]:.2f}   
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     7      ║ {coin_names[6]}        ║ $ {coin_prices_low_range[2]:.2f}    
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     8      ║ {coin_names[7]}       ║ $ {coin_prices_mid_range[3]:.2f}    
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     9      ║ {coin_names[8]}        ║ $ {coin_prices_mid_range[2]:.2f}       
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     10     ║ {coin_names[9]}      ║ $ {coin_prices_low_range[0]:.2f}      
╚════════════╩═══════════════════════════════════════════════════════════════╝
""")
    coin_to_be_purchased_name = input('🪙  TARGET ASSET ID: ') #FIX THIS MAKE SURE THAT IF THE INPUT STATEMTNS AT EMPTY IT WOULD CIRCLE BACK TO THE DEF
    if len(coin_to_be_purchased_name.strip()) == 0:
         return coins_page_buy_command()

    coin_to_be_purchased_quantity_input = input('📦 QUANITTY UNITS: ')
    if len(coin_to_be_purchased_quantity_input.strip()) == 0:
         return coins_page_buy_command()

    coin_to_be_purchased_quantity = int(coin_to_be_purchased_quantity_input)
    coin_to_be_purchased_confirmation = input('✅ AUTHORIZE PURCHASE (y/n): ')

    total = 0
    coin_name = ''

    if coin_to_be_purchased_name == '1':
        if coin_prices_high_range[0] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_high_range[0] * coin_to_be_purchased_quantity
        coin_name = 'ByteBucks'
    elif coin_to_be_purchased_name == '2':
        if coin_prices_mid_range[1] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_mid_range[1] * coin_to_be_purchased_quantity
        coin_name = "LunaMint"
    elif coin_to_be_purchased_name == '3':
        if coin_prices_mid_range[0] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_mid_range[0] * coin_to_be_purchased_quantity
        coin_name = "Vironix"
    elif coin_to_be_purchased_name == '4':
        if coin_prices_high_range[1] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_high_range[1] * coin_to_be_purchased_quantity
        coin_name = "HexaFuel"
    elif coin_to_be_purchased_name == '5':
        if coin_prices_high_range[2] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_high_range[2] * coin_to_be_purchased_quantity
        coin_name = "OpalX"
    elif coin_to_be_purchased_name == '6':
        if coin_prices_low_range[1] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_low_range[1] * coin_to_be_purchased_quantity
        coin_name = "TerraGreem"
    elif coin_to_be_purchased_name == '7':
        if coin_prices_low_range[2] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_low_range[2] * coin_to_be_purchased_quantity
        coin_name = "Lumina"
    elif coin_to_be_purchased_name == '8':
        if coin_prices_mid_range[3] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_mid_range[3] * coin_to_be_purchased_quantity
        coin_name = "Gearcoin"
    elif coin_to_be_purchased_name == '9':
        if coin_prices_mid_range[2] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_mid_range[2] * coin_to_be_purchased_quantity
        coin_name = "Cosmic"
    elif coin_to_be_purchased_name == '10':
        if coin_prices_low_range[0] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices_low_range[0] * coin_to_be_purchased_quantity
        coin_name = "Voltflux"
    else:
        print("\n❌ Invalid coin selection!")
        time.sleep(2)
        return coins_page()

    if coin_to_be_purchased_confirmation.lower() == 'y':
        if user_wallet['balance'] >= total:
            user_wallet['balance'] -= total
            if 'coins_owned' not in bag or not isinstance(bag['coins_owned'], dict):
                bag['coins_owned'] = {}
            
            if coin_name in bag['coins_owned']:
                bag['coins_owned'][coin_name] += coin_to_be_purchased_quantity
            else:
                bag['coins_owned'][coin_name] = coin_to_be_purchased_quantity
            time.sleep(1)
            os.system('cls' if os.name=='nt' else 'clear')
            print("\n\n")
            print("    ➡️ Processing digital asset order - pending network settlement confirmation...")
            time.sleep(2)
            print("    ✅ Settlement reference issued in verified - custodial release in progress...")
            time.sleep(3)
            print(f"""
╔══════════════════════════════════════════════════════════╗
║ 💳  OFFICIAL TRANSACTION RECEIPT                         ║
╠══════════════════════════════════════════════════════════╣
║ 📅 DATE & TIME   : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}                   ║
║ 🆔 TRANSACTION ID:  CHANGE THISSS                        ║
╠══════════════════════════════════════════════════════════╣
║ 💰 ASSET NAME    : {coin_to_be_purchased_name:<34}       
║ 📦 QUANTITY      : {coin_to_be_purchased_quantity:<34}   
║ 💵 TOTAL AMOUNT  : ${total:,.2f}{" " * (34 - len(f"{total:,.2f}"))}
╠══════════════════════════════════════════════════════════╣
║ ✅ STATUS        : CONFIRMED                             ║
╚══════════════════════════════════════════════════════════╝
┌─ INSTITUTIONAL SERVICES ───────────────────────────────────────────────────────┐
│ 📞 Private Banking: 1-800-CSH-PRIME │ 🌐 Research Portal: csh.com/research    │
│ 💬 Concierge: Available 24/7/365    │ 📧 Support: institutional@coinshell.com │
└────────────────────────────────────────────────────────────────────────────────┘

💰 New Balance: ${user_wallet['balance']:.2f}
""")
            time.sleep(3)
            return coins_page()
            # print('return to coins page ni sya')
        else:
            print('❌ Transaction failed: Insufficient funds!')
            time.sleep(2)
            return coins_page_buy_command()
        
    elif coin_to_be_purchased_confirmation.lower() == 'n':
        print('❌ Order Canceled!')
        time.sleep(2)
        return coins_page()

    else:
        print('❌ Command Unavailable!')
        time.sleep(2)
        return coins_page_buy_command()





def coins_page_sell_command():
    os.system('cls' if os.name=='nt' else 'clear')
    coin_names = ['|🦌| ByteBucks(BYB)', '|🌙| LunaMint(LMT)', '|🦠| Vironix(VRX)', '|⛽| HexaFuel(HXF)', '|❌| OpalX(OPX)', '|🌱| TerraGreen(TGR)', '|💡| Lumina(LMN)', '|⚙️| GearCoin(GRC)', '|🪐| Cosmic(CSC)', '|⚡️| VoltFlux(VFX)']
    print(f"""
██████████████████████████████████████████████████████████████████████████████
█ ░░░░░░░░░░░░░░░░░░░░░ OFFICIAL CRYPTO PURCHASE PORTAL ░░░░░░░░░░░░░░░░░░░░ █
██████████████████████████████████████████████████████████████████████████████
╠════════════════════════════════════════════════════════════════════════════╣
║                         📈 LIVE MARKET BOARD                               ║
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     #      ║ NAME                    ║ PRICE (USD)                         ║
╠════════════╬═════════════════════════╬═════════════════════════════════════╣
║     1      ║ {coin_names[0]}     ║ $ {coin_sell_prices_high_range[0]:.2f}
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     2      ║ {coin_names[1]}      ║ $ {coin_sell_prices_mid_range[1]:.2f}  
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     3      ║ {coin_names[2]}       ║ $ {coin_sell_prices_mid_range[ 0]:.2f}     
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     4      ║ {coin_names[3]}      ║ $ {coin_sell_prices_high_range[1]:.2f} 
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     5      ║ {coin_names[4]}         ║ $ {coin_sell_prices_high_range[2]:.2f}   
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     6      ║ {coin_names[5]}    ║ $ {coin_sell_prices_low_range[1]:.2f}   
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     7      ║ {coin_names[6]}        ║ $ {coin_sell_prices_low_range[2]:.2f}    
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     8      ║ {coin_names[7]}       ║ $ {coin_sell_prices_mid_range[3]:.2f}    
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     9      ║ {coin_names[8]}        ║ $ {coin_sell_prices_mid_range[2]:.2f}       
╠════════════╦═════════════════════════╦═════════════════════════════════════╣
║     10     ║ {coin_names[9]}      ║ $ {coin_sell_prices_low_range[0]:.2f}      
╚════════════╩═══════════════════════════════════════════════════════════════╝
""")
    coin_to_be_purchased_name = input('🪙  TARGET ASSET ID: ') #FIX THIS MAKE SURE THAT IF THE INPUT STATEMTNS AT EMPTY IT WOULD CIRCLE BACK TO THE DEF
    if len(coin_to_be_purchased_name.strip()) == 0:
         return coins_page_sell_command()

    coin_to_be_purchased_quantity_input = input('📦 QUANITTY UNITS: ')
    if len(coin_to_be_purchased_quantity_input.strip()) == 0:
         return coins_page_sell_command()

    coin_to_be_purchased_quantity = int(coin_to_be_purchased_quantity_input)
    coin_to_be_purchased_confirmation = input('✅ AUTHORIZE PURCHASE (y/n): ')

    total = 0
    coin_name = ''

    if coin_to_be_purchased_name == '1':
        total = coin_sell_prices_high_range[0] * coin_to_be_purchased_quantity
        coin_name = 'ByteBucks'
    elif coin_to_be_purchased_name == '2':
        total = coin_sell_prices_mid_range[1] * coin_to_be_purchased_quantity
        coin_name = "LunaMint"
    elif coin_to_be_purchased_name == '3':
        total = coin_sell_prices_mid_range[0] * coin_to_be_purchased_quantity
        coin_name = "Vironix"
    elif coin_to_be_purchased_name == '4':
        total = coin_sell_prices_high_range[1] * coin_to_be_purchased_quantity
        coin_name = "HexaFuel"
    elif coin_to_be_purchased_name == '5':
        total = coin_sell_prices_high_range[2] * coin_to_be_purchased_quantity
        coin_name = "OpalX"
    elif coin_to_be_purchased_name == '6':
        total = coin_sell_prices_low_range[1] * coin_to_be_purchased_quantity
        coin_name = "TerraGreem"
    elif coin_to_be_purchased_name == '7':
        total = coin_sell_prices_low_range[2] * coin_to_be_purchased_quantity
        coin_name = "Lumina"
    elif coin_to_be_purchased_name == '8':
        total = coin_sell_prices_mid_range[3] * coin_to_be_purchased_quantity
        coin_name = "Gearcoin"
    elif coin_to_be_purchased_name == '9':
        total = coin_sell_prices_mid_range[2] * coin_to_be_purchased_quantity
        coin_name = "Cosmic"
    elif coin_to_be_purchased_name == '10':
        total = coin_sell_prices_low_range[90] * coin_to_be_purchased_quantity
        coin_name = "Voltflux"
    else:
        print("\n❌ Invalid coin selection!")
        time.sleep(2)
        return coins_page()

    if coin_to_be_purchased_confirmation.lower() == 'y':
        if coin_name in bag['coins_owned'] and coin_to_be_purchased_quantity <= bag['coins_owned'][coin_name]:
            bag['coins_owned'][coin_name] += coin_to_be_purchased_quantity

            if bag['coins_owned'][coin_name] == 0:
                del bag['coins_owned'][coin_name]

            user_wallet['balance'] += total
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        print("\n\n")
        print("    ➡️ Initiating blockchain consensus protocol - awaiting validator signatures...")
        time.sleep(2)
        print("    ✅ Consensus achieved - smart contract execution and asset transfer authorized...")
        time.sleep(3)
        print(f"""
╔══════════════════════════════════════════════════════════╗
║ 💳  OFFICIAL TRANSACTION RECEIPT                         ║
╠══════════════════════════════════════════════════════════╣
║ 📅 DATE & TIME   : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}                   ║
║ 🆔 TRANSACTION ID:  CHANGE THISSS                        ║
╠══════════════════════════════════════════════════════════╣
║ 💰 ASSET NAME    : {coin_to_be_purchased_name:<34}       
║ 📦 QUANTITY      : {coin_to_be_purchased_quantity:<34}   
║ 💵 TOTAL AMOUNT  : ${total:,.2f}{" " * (34 - len(f"{total:,.2f}"))}
╠══════════════════════════════════════════════════════════╣
║ ✅ STATUS        : CONFIRMED                             ║
╚══════════════════════════════════════════════════════════╝
┌─ INSTITUTIONAL SERVICES ───────────────────────────────────────────────────────┐
│ 📞 Private Banking: 1-800-CSH-PRIME │ 🌐 Research Portal: csh.com/research    │
│ 💬 Concierge: Available 24/7/365    │ 📧 Support: institutional@coinshell.com │
└────────────────────────────────────────────────────────────────────────────────┘

💰 New Balance: ${user_wallet['balance']:.2f}
""")

        time.sleep(3)
        return coins_page()


    elif coin_to_be_purchased_confirmation.lower() == 'n':
        print('❌ Order Canceled!')
        time.sleep(2)
        return coins_page()

    else:
        print('❌ Command Unavailable!')
        time.sleep(2)
        return coins_page()





#STARTING MESSAGE
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

                                                                                    💵 Starting Balance: $100
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
    for i in range(2): #CHANGE THIS SHIT BACK TO 100
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
                print(f'💰 Wallet Balance: ${user_wallet['balance']:.2f}')
                print(f'🎒 Inventory: {bag['coins_owned']}')
                fake_news.fake_news()
        
                        


                user_dashboard_choice = input("""\n(v) 📊 View portfolio  |  (b) 🕳️  Black market   |   (m) 📈 View market  |  (r) 🪙 Purchase/sell coins  |  (e) 🚪 Exit                       
""").strip().lower()
                if user_dashboard_choice == 'v':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('portfolio logic')
                elif user_dashboard_choice == 'b':
                        black_market_page()
                elif user_dashboard_choice == 'm':
                        print('market logic')
                elif user_dashboard_choice == 'r':
                        coins_page()
                elif user_dashboard_choice == 'e':
                        break
                else:
                        print('Command Unavailable')
