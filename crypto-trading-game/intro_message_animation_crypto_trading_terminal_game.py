import time
import sys
import os
import math
a = """
  /$$$$$$            /$$              /$$    /$$                 /$$ /$$
 /$$__  $$          |__/            /$$$$$$ | $$                | $$| $$
| $$  \__/  /$$$$$$  /$$ /$$$$$$$  /$$__  $$| $$$$$$$   /$$$$$$ | $$| $$
| $$       /$$__  $$| $$| $$__  $$| $$  \__/| $$__  $$ /$$__  $$| $$| $$
| $$      | $$  \ $$| $$| $$  \ $$|  $$$$$$ | $$  \ $$| $$$$$$$$| $$| $$
| $$    $$| $$  | $$| $$| $$  | $$ \____  $$| $$  | $$| $$_____/| $$| $$
|  $$$$$$/|  $$$$$$/| $$| $$  | $$ /$$  \ $$| $$  | $$|  $$$$$$$| $$| $$
 \______/  \______/ |__/|__/  |__/|  $$$$$$/|__/  |__/ \_______/|__/|__/
                                   \_  $$_/                             
                                     \__/ """

def introanimate(delay=0.07):
    lines = a.splitlines()
    t = 0
    for _ in range(30):
        os.system('cls' if os.name=='nt' else 'clear')
        for j, line in enumerate(lines):

            offset = int(5 * math.sin(t + j * 0.5))
            print(" " * offset + line)
            pass
        time.sleep(delay)
        t += 0.3
