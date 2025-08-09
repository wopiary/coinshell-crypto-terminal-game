import os
import time
import sys
import random
import threading
import fake_news
import line_graph
import string

#GLOBAL
user_wallet = {
       'balance': 500.00
}
Name = None
# coin_prices = [random.uniform(1.0, 1000.0) for _ in range(14)]
bag = {
      'coins_owned': []
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

def updates_coin_prices(): 
      global coin_prices
      coin_prices = [random.uniform(-1000.0, 400.0) for _ in range(14)]


# 'B' COMMAND

black_market_page_product_category = [
    "Crypto Exchange",
    "Compromised Coinshell Accounts",
    "Misc. Black Market Goods",
    "Exit Silk Claw"
]
def black_market_page_generate_key(length =6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def black_market_page():
    global user_wallet
    os.system('cls' if os.name == 'nt' else 'clear')

    
    
    # # Spooky loading effect
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
      Account: ANON-{account_num} │ Clearance Level: OMEGA
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
        time.sleep(1.5)


def black_market_page_crypto_coin():
            os.system('cls' if os.name=='nt' else 'clear')
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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CRYPTO EXCHANGE NODE] — SILK CLAW MARKETPLACE v3.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: ACTIVE │ Wallet Integration: ENABLED │ Escrow: SECURED
Wallet: ${user_wallet['balance']:.2f}
──────────────────────────────────────────────────────────────────────
 ID   │ ITEM/DESCRIPTION                  │ PRICE 
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
            black_market_page_user_input = input('Enter your choice:')



# 'R' COMMAND, BUYING AND SELLING
def coins_page():
    global user_wallet
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    coin_names = ['|🦌| ByteBucks(BYB)', '|🌙| LunaMint(LMT)', '|🦠| Vironix(VRX)', '|⛽| HexaFuel(HXF)', '|❌| OpalX(OPX)', '|🌱| TerraGreen(TGR)', '|💡| Lumina(LMN)', '|⚙️| GearCoin(GRC)', '|🪐| Cosmic(CSC)', '|⚡️| VoltFlux(VFX)']
    
    global coin_prices

    print(f"""• Market Board
                 #  | COIN NAME                | VALUE ($)      
          ----------|--------------------------|----------------
                (1) | {coin_names[0]}      | ${coin_prices[0]:.5f}
          ----------|--------------------------|----------------
                (2) | {coin_names[1]}       | ${coin_prices[1]:.5f}
          ----------|--------------------------|----------------
                (3) | {coin_names[2]}        | ${coin_prices[2]:.5f}
          ----------|--------------------------|----------------
                (4) | {coin_names[3]}       | ${coin_prices[3]:.5f}
          ----------|--------------------------|----------------
                (5) | {coin_names[4]}          | ${coin_prices[4]:.5f}
          ----------|--------------------------|----------------
                (6) | {coin_names[5]}     | ${coin_prices[5]:.5f}
          ----------|--------------------------|----------------
                (7) | {coin_names[6]}         | ${coin_prices[6]:.5f}
          ----------|--------------------------|----------------
                (8) | {coin_names[7]}        | ${coin_prices[7]:.5f}
          ----------|--------------------------|----------------
                (9) | {coin_names[8]}         | ${coin_prices[8]:.5f}
          ----------|--------------------------|----------------
                (10)| {coin_names[9]}       | ${coin_prices[9]:.5f}

""")
    print(f'💰 Wallet Balance: {user_wallet['balance']:.2f}')
    print(f'🎒 Inventory: {bag['coins_owned']}')
        
    coins_page_dashboard_choice = input(
"""(b) 🟢 Buy  |  🔴 (s) Sell  |  🚪 (e) Return to Home
""")
     
        
    if coins_page_dashboard_choice == 'b':
               coins_page_buy_command()
    elif coins_page_dashboard_choice == 's':
               coins_page_sell_command()
    elif coins_page_dashboard_choice == 'e':
               return 'back'






def coins_page_buy_command():
    global coin_prices
    print("""
╒══════════════════════════════════════════════════╕
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
│░            Coin$hell Payment Portal            ░│
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
├──────────────────────────────────────────────────┤
│      please enter the following information      │
╘══════════════════════════════════════════════════╛
""")
    coin_to_be_purchased_name = input('💎 Coin #: ')
    coin_to_be_purchased_quantity = int(input('📦 Quantity: '))
    coin_to_be_purchased_confirmation = input('✅ Confirm purchase (y/n): ')

    total = 0
    coin_name = ''

    if coin_to_be_purchased_name == '1':
        if coin_prices[0] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[0] * coin_to_be_purchased_quantity
        coin_name = 'ByteBucks'
    elif coin_to_be_purchased_name == '2':
        if coin_prices[1] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[1] * coin_to_be_purchased_quantity
        coin_name = "LunaMint"
    elif coin_to_be_purchased_name == '3':
        if coin_prices[2] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[2] * coin_to_be_purchased_quantity
        coin_name = "Vironix"
    elif coin_to_be_purchased_name == '4':
        if coin_prices[3] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[3] * coin_to_be_purchased_quantity
        coin_name = "HexaFuel"
    elif coin_to_be_purchased_name == '5':
        if coin_prices[4] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[4] * coin_to_be_purchased_quantity
        coin_name = "OpalX"
    elif coin_to_be_purchased_name == '6':
        if coin_prices[5] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[5] * coin_to_be_purchased_quantity
        coin_name = "TerraGreem"
    elif coin_to_be_purchased_name == '7':
        if coin_prices[6] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[6] * coin_to_be_purchased_quantity
        coin_name = "Lumina"
    elif coin_to_be_purchased_name == '8':
        if coin_prices[7] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[7] * coin_to_be_purchased_quantity
        coin_name = "Gearcoin"
    elif coin_to_be_purchased_name == '9':
        if coin_prices[8] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[8] * coin_to_be_purchased_quantity
        coin_name = "Cosmic"
    elif coin_to_be_purchased_name == '10':
        if coin_prices[9] <= 0:
            print('❌ Transaction failed: Cannot buy a coin with a value of $0 or less.')
            time.sleep(2)
            return
        total = coin_prices[9] * coin_to_be_purchased_quantity
        coin_name = "Voltflux"
    else:
        print("Invalid coin selection!")
        return

    if coin_to_be_purchased_confirmation.lower() == 'y':
        if user_wallet['balance'] >= total:
            user_wallet['balance'] -= total
            if 'coins_owned' not in bag or not isinstance(bag['coins_owned'], dict):
                bag['coins_owned'] = {}
            
            if coin_name in bag['coins_owned']:
                bag['coins_owned'][coin_name] += coin_to_be_purchased_quantity
            else:
                bag['coins_owned'][coin_name] = coin_to_be_purchased_quantity
            print(f"""
╔═══════════════════════════════════════╗
║   🚀✨ TRANSACTION SUCCESSFUL! ✨🚀   ║
║         🧾 Buyer's Receipt            ║ 
╠═══════════════════════════════════════╣
║ 💎 Coin #: {coin_to_be_purchased_name} | Qty: {coin_to_be_purchased_quantity} | Total: ${total:.2f}║
║ ✅ Status: CONFIRMED                  ║
║ 🚀 Thanks for trading with Coin$hell! ║
╚═══════════════════════════════════════╝

💰 New Balance: ${user_wallet['balance']:.2f}
""")
            time.sleep(2)
        else:
            print('❌ Transaction failed: Insufficient funds!')
            time.sleep(2)
    elif coin_to_be_purchased_confirmation.lower() == 'n':
        print('❌ Order Canceled!')
    else:
        print('❌ Command Unavailable!')

def coins_page_sell_command():
    print("""
╒══════════════════════════════════════════════════╕
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
│░             Coin$hell Sale Portal              ░│
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
├──────────────────────────────────────────────────┤
│        please enter the following information    │
╘══════════════════════════════════════════════════╛
""")
    coin_to_be_purchased_name = input('💎 Coin #: ')
    coin_to_be_purchased_quantity = int(input('📦 Quantity: '))
    coin_to_be_purchased_confirmation = input('✅ Confirm purchase (y/n): ')

    total = 0
    coin_name = ''
    if coin_to_be_purchased_name == '1':
        total = coin_prices[0] * coin_to_be_purchased_quantity
        coin_name = 'ByteBucks'
    elif coin_to_be_purchased_name == '2':
        total = coin_prices[1] * coin_to_be_purchased_quantity
        coin_name = "LunaMint"
    elif coin_to_be_purchased_name == '3':
        total = coin_prices[2] * coin_to_be_purchased_quantity
        coin_name = "Vironix"
    elif coin_to_be_purchased_name == '4':
        total = coin_prices[3] * coin_to_be_purchased_quantity
        coin_name = "HexaFuel"
    elif coin_to_be_purchased_name == '5':
        total = coin_prices[4] * coin_to_be_purchased_quantity
        coin_name = "OpalX"
    elif coin_to_be_purchased_name == '6':
        total = coin_prices[5] * coin_to_be_purchased_quantity
        coin_name = "TerraGreem"
    elif coin_to_be_purchased_name == '7':
        total = coin_prices[6] * coin_to_be_purchased_quantity
        coin_name = "Lumina"
    elif coin_to_be_purchased_name == '8':
        total = coin_prices[7] * coin_to_be_purchased_quantity
        coin_name = "Gearcoin"
    elif coin_to_be_purchased_name == '9':
        total = coin_prices[8] * coin_to_be_purchased_quantity
        coin_name = "Cosmic"
    elif coin_to_be_purchased_name == '10':
        total = coin_prices[9] * coin_to_be_purchased_quantity
        coin_name = "Voltflux"
    else:
        print("Invalid coin selection!")
        return

    if coin_to_be_purchased_confirmation.lower() == 'y':
        if coin_name in bag['coins_owned'] and coin_to_be_purchased_quantity <= bag['coins_owned'][coin_name]:
            bag['coins_owned'][coin_name] -= coin_to_be_purchased_quantity

            if bag['coins_owned'][coin_name] == 0:
                del bag['coins_owned'][coin_name]

            user_wallet['balance'] += total

            print(f"""
    ╔═══════════════════════════════════════╗
    ║  🚀✨ TRANSACTION SUCCESSFUL! ✨🚀   ║
    ║        🧾 Seller's Receipt         ║ 
    ╠═══════════════════════════════════════╣
    ║ 💎 Coin #: {coin_to_be_purchased_name} | Qty: {coin_to_be_purchased_quantity} | Total: ${total:.2f}║
    ║ ✅ Status: CONFIRMED                  ║
    ║ 🚀 Thanks for trading with Coin$hell! ║
    ╚═══════════════════════════════════════╝

    💰 New Balance: ${user_wallet['balance']:.2f}
""")
        else:
            print('❌ Transaction failed: Coins Not in Inventory!')

            time.sleep(2)
    elif coin_to_be_purchased_confirmation.lower() == 'n':
        print('❌ Order Canceled!')
    else:
        print('❌ Command Unavailable!')





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
                        updates_coin_prices()
                        coins_page()
                elif user_dashboard_choice == 'e':
                        break
                else:
                        print('Command Unavailable')
