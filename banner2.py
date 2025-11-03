
#modluse of script
import os
import sys
import time
import random
import datetime

#color's'

GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'

# banner of script
banner = r"""
                  .-"      "-.
                 /            \
                |,  .-.  .-.  ,|     KINGHacker
                | )(_o/  \o_)( |     TORK
                |/     /\     \|     TORBAT
                (_     ^^     _)     SINA&M
                 \__|IIIIII|__/
                  | \IIIIII/ |
                  \          /
                   `--------'
██╗  ██╗██╗███╗   ██╗ ██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║ ██╔╝██║████╗  ██║██╔═══██╗██║ ██╔╝██╔══██╗██╔════╝██║ ██╔╝
█████╔╝ ██║██╔██╗ ██║██║   ██║█████╔╝ ███████║██║     █████╔╝ 
██╔═██╗ ██║██║╚██╗██║██║   ██║██╔═██╗ ██╔══██║██║     ██╔═██╗ 
██║  ██╗██║██║ ╚████║╚██████╔╝██║  ██╗██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

# Matrix 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()"
columns = 80
rows = 24
drops = [0 for _ in range(columns)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(GREEN + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_rain(duration=8):
    start_time = time.time()
    while time.time() - start_time < duration:
        clear_screen()
        print(GREEN + banner + RESET)
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{GREEN}Time: {time_str}{RESET}\n")
        for i in range(rows - 10):
            line = ""
            for j in range(columns):
                if drops[j] == i:
                    line += random.choice(chars)
                else:
                    line += " "
            print(GREEN + line + RESET)
        drops[:] = [drop + 1 if drop < rows else 0 for drop in drops]
        time.sleep(0.005)

def fake_hacking():
    targets = ["SERVER_01", "DATABASE_ALPHA", "FIREWALL_X", "NETWORK_NODE_7"]
    actions = ["Connecting", "Bypassing security", "Decrypting", "Injecting payload", "Access Granted"]

    slow_print("\n>>> Kinghacker HACK SIMULATOR <<<\n", 0.003)
    time.sleep(1)

    for target in targets:
        for action in actions:
            slow_print(f"{action} on {target}...", 0.02)
            time.sleep(random.uniform(0.1, 0.4))

     #time
    for i in range(5, 0, -1):
        slow_print(f"{RED}!!! ALERT: Firewall Breach in {i} !!!{RESET}", 0.02)
        time.sleep(0.02)

    slow_print(f"\n{GREEN}>>> HACKING COMPLETE <<<\n", 0.03)

if __name__ == "__main__":
    try:
        matrix_rain(duration=10)
        fake_hacking()
        slow_print(f"{GREEN}>>> Kinghacker SESSION ENDED <<<", 0.03)
    except KeyboardInterrupt:
        slow_print("\n>>> Exiting Kinghacker <<<", 0.03)
        sys.exit()
        
