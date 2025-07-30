import os
import time
import sys
import random
import threading


        


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
        
    
    print("Loading market data...")
    
    spinner = '-\\|/'
    for i in range(1): #CHANGE THIS SHIT BACK TO 100
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
                
                print('• Market LIVE!\n')
                print(f'{random.choice([        """
$1200 ┤                                    ╭─╮
$1150 ┤                               ╭────╯  ╰╮
$1100 ┤                          ╭────╯        ╰╮
$1050 ┤                     ╭────╯              ╰─╮
$1000 ┤                ╭────╯                    ╰╮
$ 950 ┤           ╭────╯                          ╰─╮
$ 900 ┤      ╭────╯                                ╰╮
$ 850 ┤ ╭────╯                                      ╰──
$ 800 ┴─╯                                              
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",


        """
$1200 ┤╭─╮                                      
$1150 ┤╯  ╰╮                                     
$1100 ┤    ╰╮                ╭─╮                 
$1050 ┤     ╰─╮         ╭────╯  ╰╮               
$1000 ┤       ╰╮   ╭────╯        ╰╮              
$ 950 ┤        ╰─╮╱╯              ╰─╮            
$ 900 ┤          ╰╯                 ╰╮           
$ 850 ┤                              ╰─╮        
$ 800 ┴─                               ╰────────
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",


        """
$1200 ┤    ╭─╮              ╭─╮              
$1150 ┤   ╱   ╰╮        ╭────╯  ╰╮             
$1100 ┤  ╱     ╰╮  ╭────╯        ╰╮            
$1050 ┤ ╱       ╰─╱╯              ╰─╮          
$1000 ┤╱                            ╰╮         
$ 950 ┤                              ╰─╮       
$ 900 ┤                                ╰╮      
$ 850 ┤                                 ╰─╮    
$ 800 ┴─                                  ╰────
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",


        """
$1200 ┤         ╭─╮     ╭─╮               
$1150 ┤    ╭────╯  ╰╮   ╱   ╰╮              
$1100 ┤   ╱         ╰╮ ╱     ╰╮             
$1050 ┤  ╱           ╰╱       ╰─╮           
$1000 ┤ ╱                      ╰╮          
$ 950 ┤╱                        ╰─╮        
$ 900 ┤                           ╰╮       
$ 850 ┤                            ╰─╮     
$ 800 ┴─                             ╰─────
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",


        """
$1200 ┤           ╭╮                      
$1150 ┤          ╱  ╲                     
$1100 ┤         ╱    ╲                    
$1050 ┤        ╱      ╲                   
$1000 ┤   ╭───╱        ╲                  
$ 950 ┤  ╱             ╲                 
$ 900 ┤ ╱               ╲╲               
$ 850 ┤╱                 ╲╲              
$ 800 ┴─                  ╲╲─────────────
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",


        """
$1200 ┤                          ╭──────╮
$1150 ┤                     ╭────╯       ╰╮
$1100 ┤                ╭────╯             ╰╮
$1050 ┤           ╭────╯                   ╰─╮
$1000 ┤      ╭────╯                         ╰╮
$ 950 ┤ ╭────╯                              ╰─╮
$ 900 ┤╱╯                                    ╰╮
$ 850 ┤                                       ╰─╮
$ 800 ┴─                                        ╰──
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",


        """
$1200 ┤╭╮                                  
$1150 ┤╯ ╲                                 
$1100 ┤   ╲                                
$1050 ┤    ╲                               
$1000 ┤     ╲                              
$ 950 ┤      ╲                             
$ 900 ┤       ╲                            
$ 850 ┤        ╲╲                          
$ 800 ┴─        ╲╲─────────────────────────
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM""",

 
        """
	    ╭─╮          ╭─╮              
$1150 ┤   ╱   ╰╮    ╭───╯  ╰╮             
$1100 ┤  ╱     ╰╮  ╱        ╰╮            
$1050 ┤ ╱       ╰─╱          ╰─╮          
$1000 ┤╱                      ╰╮         
$ 950 ┤                        ╰─╮       
$ 900 ┤                          ╰╮      
$ 850 ┤                           ╰─╮    
$ 800 ┴─                            ╰────
      12PM   1PM   2PM   3PM   4PM   5PM   6PM   7PM"""])}')
                print()
                print()
                print(f'💰 Wallet Balance: {user_balance}')
                print(f'📰 News: {random.choice([
        "A trader mistook a rugpull for a feature.",
        "A DAO member explained tokenomics using emojis only.",
        "A trader sent all the ETH to a food delivery app.",
        "The CEO tried to stake coins on a microwave.",
        "A guy sold all his tokens to buy one of those chairs that folds into a cube.",
        "The CEO of a crypto startup turned out to be a Roomba with a Twitter account.",
        "A DAO voted to buy a Lambo, but it got repo'd before delivery.",
        "The CFO of a DeFi project accidentally sent $3 million to his mom.",
        "The CFO announced the whitepaper as an NFT poem.",
        "The intern left the project to become a DJ.",
        "An influencer accidentally deleted the treasury.",
        "The dev team leaked the private key live on Twitch.",
        "A crypto influencer got arrested for staking coins at a McDonald’s self-checkout.",
        "A dev got banned from his own project after using the whitepaper as a napkin.",
        "The founder hosted a presale on Club Penguin.",
        "A whale used the company funds to buy a blimp.",
        "The founder bragged about losses as a tax write-off.",
        "An NFT rug happened mid-livestream while the founder was eating Cheetos.",
        "Police shut down a mining farm powered by a hamster wheel and hopes.",
        "The team behind a coin said it 'stopped working' because Mercury's in retrograde.",
        "The CEO explained tokenomics using crayons and got a standing ovation.",
        "A guy lost $40k after copy-pasting a fake wallet address from a meme page.",
        "Crypto crashed because someone sneezed during a whale transaction.",
        "A token launched today and rugpulled before anyone could figure out the name.",
        "An airdrop went wrong — now 200 users own the same JPEG of a banana.",
        "The devs admitted their entire roadmap was generated by ChatGPT and a dream.",
        "An NFT collection got canceled because all the art was just rotated fidget spinners.",
        "Someone staked 10 ETH and accidentally adopted a goat.",
        "The founder used the roadmap as a dinner menu.",
        "A trader printed NFTs on cereal boxes.",
        "The CEO thought liquidity meant Gatorade.",
        "A DAO member burned all tokens to summon 'market spirits'.",
        "The dev team used a QR code tattoo for wallet access.",
        "A CEO explained staking as 'just chilling but with coins'.",
        "The intern confused gas fees with actual gasoline.",
        "A founder tried to short Dogecoin at a gas station.",
        "The devs hired a psychic to write their smart contract.",
        "An investor left after realizing DeFi wasn't a dessert.",
        "A trader thought cold wallet meant keeping coins in a freezer.",
        "The CEO gave a TED Talk entirely in meme gifs.",
        "A whale launched a coin called $HODLMEPLZ as a prank — now it's worth $7 million.",
        "The lead dev outsourced the blockchain to a Minecraft server.",
        "The founder mistook NFTs for NFTs (Nice Funny Tweets).",
        "An exchange accidentally listed Chuck E. Cheese tokens as a new altcoin.",
        "The CEO launched a metaverse project using Microsoft Paint.",
        "A DeFi project based its governance system on rock-paper-scissors.",
        "The intern thought smart contracts required a diploma.",
        "A dev confessed the project was inspired by a dream about spaghetti.",
        "A DAO spent all its funds on anime body pillows and now owes taxes.",
        "The CFO replaced the whitepaper with a BuzzFeed quiz.",
        "A new token's utility was just 'vibes and community'.",
        "The founder YOLO’d company reserves into meme stocks by accident.",
        "A project offered free tokens to anyone who could beat the dev in Mario Kart.",
        "An NFT was minted with a typo that made it legally a sandwich.",
        "The dev team used an AI chatbot to manage treasury decisions.",
        "A CEO declared a financial emergency due to 'bad aura on-chain'.",
        "A new project rugged itself just to prove a point.",
        "A whale rage-bought 1000 NFTs because someone called them mid.",
        "An influencer lost their cold wallet in a vending machine.",
        "A dev streamed their wallet passphrase and called it 'open source'.",
        "A project revealed their roadmap was just the word 'moon' written 12 times.",
        "A DAO tried to buy the moon and ended up buying a cheese factory.",
        "The CEO accidentally swapped $2 million into Roblox credits.",
        "The intern sent ETH to a username instead of a wallet address.",
        "A protocol changed its name mid-launch because the founder forgot the password.",
        "A security audit revealed the whole codebase was ChatGPT output.",
        "The project halted because the founder's pet parrot flew off with the seed phrase.",
        "A founder printed the entire blockchain to prove it's 'real'.",
        "The CFO turned tokenomics into a rap song and got signed.",
        "A new coin based its liquidity on 'vibes, tea leaves, and astrology'.",
        "A smart contract froze because it got stage fright on launch day.",
        "The whitepaper was a PowerPoint filled with Minion memes.",
        "A whale said he buys based on 'how the chart smells today'.",
        "A trader rage-quit after discovering his NFTs were just screenshots of his own posts.",
        "The dev forgot to deploy the contract and blamed it on solar flares.",
        "A protocol hired a magician as their lead security advisor.",
        "An NFT dropped based on crypto bros’ daily outfit selfies.",
        "A project launched a stablecoin backed by pizza coupons.",
        "A hacker refunded users because they said the code 'was too sad to exploit'.",
        "The CEO mistook testnet funds for real money and resigned.",
        "A founder confused APR with 'apricots per reward'.",
        "The DAO voted to rename the project to 'Boaty McBlockface'.",
        "An influencer invested in a scam token thinking it was a dating app.",
        "The treasury got drained after someone clicked a phishing link that said 'free V-Bucks'.",
        "A dev accidentally bricked the project by typing 'sudo destroy world'.",
        "The CEO thought 'proof of stake' meant BBQ season.",
        "An NFT platform lost $1M after hosting a 'gasless mint' that was actually just free.",
        "A blockchain-based dating app matched all users with a bot named Kevin.",
        "A founder live-tweeted his own token crash with crying emojis.",
        "The project was built entirely on Notion and vibes.",
        "A whale sold his entire portfolio to buy a PS6 prototype.",
        "A DeFi farm offered 10,000% APY — in Chuck E. Cheese tickets.",
        "An intern rugged the project just to win a dare on Discord.",
        "The roadmap was a Denny’s menu with coin names written in ketchup.",
        "A crypto CEO launched a side project to mine likes on LinkedIn.",
        "An investor thought gas fees were tips for validators.",
        "The lead dev’s resignation letter was just the word 'bruh'.",
        "The founder used the company laptop to mine Dogecoin and cook ramen.",
        "The official Discord got taken over by a cat walking on the keyboard."
        
    ]
        )}')
                        


                user_dashboard_choice = input("""(v) 📊 View portfolio  |  (m) 📈 View market  |  (r) 🪙 Purchase/sell coins  |  (e) 🚪 Exit                       
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
