from colorama import Fore, init, Style
import subprocess
import requests
import ctypes
import os

def Auth():
    r = requests.get('https://pastebin.com/raw/...').content #Raw Pastebin URL where the HWIDs will be stored
    HWID = subprocess.check_output(
        'wmic csproduct get uuid').decode().split('\n')[1].strip()
    data = bytes((HWID), encoding='UTF-8')
    if data in r:
        pass
    else:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW('Unauthorized')
        print(Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'HWID unauthorized!')
        print(Style.RESET_ALL + Fore.RED + ' -- ' + Fore.WHITE + Style.BRIGHT + 'Your HWID: ' + HWID)
        input()
        quit()
        
Auth()
#Put your code here
