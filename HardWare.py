import os
import pystyle
import ctypes
import sys
from pystyle import *

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_console()

if os.name == 'nt':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)

banner = '''


                                 ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗
                                 ██║  ██║██╔══██╗██╔══██╗██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝
                                 ███████║███████║██████╔╝██║  ██║██║ █╗ ██║███████║██████╔╝█████╗  
                                 ██╔══██║██╔══██║██╔══██╗██║  ██║██║███╗██║██╔══██║██╔══██╗██╔══╝  
                                 ██║  ██║██║  ██║██║  ██║██████╔╝╚███╔███╔╝██║  ██║██║  ██║███████╗
                                 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                                                                 
                                                           Version 1.0                                                          
                             ┌──────────────────────────────────────────────────────────────────────────┐
                             │                           Author: qqvx                                   │
                             │──────────────────────────────────────────────────────────────────────────│
                             │             Youtube @qqvxov       Telegram: @channel_qqvx                │
                             └──────────────────────────────────────────────────────────────────────────┘     
                      ┌───────────────────────────┐ ┌───────────────────────────┐ ┌───────────────────────────┐
                      │ [1] IP Founder            │ │ [12] Facebook             │ │ [23] Soon...              │
                      │ [2] Phone Lookup          │ │ [13] System               │ │ [24] Soon...              │
                      │ [3] URL Analysis          │ │ [14] Web Spider           │ │ [25] Soon...              │
                      │ [4] Phishing Builder      │ │ [15] Ultra PHL            │ │ [26] Soon...              │
                      │ [5] Parsing               │ │ [16] IPLogger             │ │ [27] Soon...              │
                      │ [6] Pentest               │ │ [17] Soon...              │ │ [28] Soon...              │
                      │ [7] Bots Osint            │ │ [18] Soon...              │ │ [29] Soon...              │
                      │ [8] Car Search            │ │ [19] Soon...              │ │ [30] Soon...              │
                      │ [9] Card Code             │ │ [20] Soon...              │ │ [31] Soon...              │
                      │ [10] Brute                │ │ [21] Soon...              │ │ [32] Soon...              │                    
                      │ [11] Brute Email          │ │ [22] Soon...              │ │ [33] Soon...              │
                      └───────────────────────────┘ └───────────────────────────┘ └───────────────────────────┘
                                                                                             ┌────────────────┐
                                                                                             │ [34] Developer │
                                                                                             └────────────────┘
                                                                                  
'''

Write.Print(banner, Colors.green_to_cyan, interval=0.000005)

while True:
    sys.stdout.write(f"\x1b]2;[\] HardWare :: Online Users: [1] :: Status Active: [10/10]\x07")
    sin = input("\033[1;37;41mHardWare@PANEL\x1b[0m:~# \x1b[0m")
    
    if sin == "1":
        os.system("Components\\ip_founder.py")  
    elif sin == "0":
        print("Выход...")
        break  
    else:
        print("Запускаю...")
    if sin == "2":
        os.system("Components\\phone_lookup.py")  
    elif sin == "0":
        print("Выход...")
        break  
    else:
        print("Запускаю...")
    if sin == "3":
        os.system("Components\\information_sites.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "4":
        os.system("Components\\builder.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "10":
        os.system("Components\\bruteforce.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "11":
        os.system("Components\\bruteforce_email.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "5":
        os.system("Components\\Parsing.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "6":
        os.system("Components\\pentest.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "7":
        os.system("Components\\bots_osint.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "8":
        os.system("Components\\car_search.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "9":
        os.system("Components\\card_code.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "12":
        os.system("Components\\facebook.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "13":
        os.system("Components\\system.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "34":
        os.system("Components\\developer.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "14":
        os.system("Components\\web_spider.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "15":
        os.system("Components\\phone_lookup-main\\phone_lookup.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")
    if sin == "16":
        os.system("Components\\IPLogger-main\\IPLogger.py")  
    elif sin == "0":
        print("Выход...")
        break 
    else:
        print("Запускаю...")

