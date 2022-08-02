# Coded by ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################

import os
import re
import sys
import shutil
import requests
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup
from colorama import Fore

from utilities.Settings.common import *

#########################################

def search_for_updates():
    clear()
    setTitle("UPDATE AVAILABLE !!")
    r = requests.get("https://github.com/TT-Tutorials/GANG-Nuker/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        Write.Print("\n\n\n          ▐ ▄ ▄▄▄ .▄▄▌ ▐ ▄▌    ▄• ▄▌ ▄▄▄··▄▄▄▄   ▄▄▄· ▄▄▄▄▄▄▄▄ .\n", Colors.white_to_green, interval=0.000)   
        Write.Print("         •█▌▐█▀▄.▀·██· █▌▐█    █▪██▌▐█ ▄███▪ ██ ▐█ ▀█ •██  ▀▄.▀·\n", Colors.white_to_green, interval=0.000)   
        Write.Print("         ▐█▐▐▌▐▀▀▪▄██▪▐█▐▐▌    █▌▐█▌ ██▀·▐█· ▐█▌▄█▀▀█  ▐█.▪▐▀▀▪▄\n", Colors.white_to_green, interval=0.000)      
        Write.Print("         ██▐█▌▐█▄▄▌▐█▌██▐█▌    ▐█▄█▌▐█▪·•██. ██ ▐█ ▪▐▌ ▐█▌·▐█▄▄▌\n", Colors.white_to_green, interval=0.000)
        Write.Print("         ▀▀ █▪ ▀▀▀  ▀▀▀▀ ▀▪     ▀▀▀ .▀   ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀▀▀ \n", Colors.white_to_green, interval=0.000)
        print(f'''\n\n                               {Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}]{Fore.WHITE} LOG-YY [{Fore.GREEN}{THIS_VERSION}{Fore.WHITE}] is OUTDATED !!''')
        soup = BeautifulSoup(requests.get("https://github.com/TT-Tutorials/GANG-Nuker/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        print(f'                               {Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}]{Fore.WHITE} Would You Like To Update To The Latest Version?')
        choice = input(f'                               {Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}]{Fore.WHITE} (Y/N)?: ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n                               {Fore.WHITE}[{Fore.GREEN}/{Fore.WHITE}]{Fore.WHITE} Updating LOG-YY Nuker !!")

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("GANG-Nuker.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("GANG-Nuker.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("GANG-Nuker.zip")
                cwd = os.getcwd()+'\\GANG-Nuker\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'GANG-Nuker.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('GANG-Nuker')
                input(f"                               {y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!", end="")
                os.startfile("GANG-Nuker.exe")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/TT-Tutorials/GANG-Nuker/archive/refs/heads/master.zip")
                with open("GANG-Nuker-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("GANG-Nuker-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("GANG-Nuker-main.zip")
                cwd = os.getcwd()+'\\GANG-Nuker-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                input(f"                               {y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!")
                if os.path.exists(os.getcwd()+'setup.bat'):
                    os.startfile("setup.bat")
                elif os.path.exists(os.getcwd()+'start.bat'):
                    os.startfile("start.bat")
                os._exit(0)