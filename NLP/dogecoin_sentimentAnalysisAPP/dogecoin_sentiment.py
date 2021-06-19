from os import truncate
import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
#Dogecoin Analysis header
print('+_____________________________________________________________________________________+')
print('|  _____                             _                              _           _     |')
print('| |  __ \                           (_)           /\               | |         (_)    |')
print('| | |  | | ___   __ _  ___  ___ ___  _ _ __      /  \   _ __   __ _| |_   _ ___ _ ___ |')
print('| | |  | |/ _ \ / _  |/ _ \/ __/ _ \| |  _ \    / /\ \ |  _ \ / _  | | | | / __| / __||')
print('| | |__| | (_) | (_| |  __/ (_| (_) | | | | |  / ____ \| | | | (_| | | |_| \__ \ \__ \|')
print('| |_____/ \___/ \__, |\___|\___\___/|_|_| |_| /_/    \_\_| |_|\__,_|_|\__, |___/_|___/|')
print('|                __/ |                                                 __/ |          |')
print('|               |___/                                                 |___/           |')
print('+_____________________________________________________________________________________+')
print('')
print('                                   ▄              ▄')
print('                                  ▌▒█           ▄▀▒▌')
print('                                  ▌▒▒█        ▄▀▒▒▒▐')
print('                                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐')
print('                               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐')
print('                             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌')
print('                            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌')
print('                            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐')
print('                           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌')
print('                           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌')
print('                          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐')
print('                          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌')
print('                          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐')
print('                           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌')
print('                           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐')
print('                            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌')
print('                              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀')
print('                                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀')
print('                                   ▒▒▒▒▒▒▒▒▒▒▀▀')



#twitter keys order
# 1. API Key
# 2. API Secret Key
# 3. Access Token
# 4. Access secret Token

#Collects the parameters from keys.txt file
twiterkeys = open('keys.txt' , 'r').read().splitlines()
api_key =            twiterkeys [0]
secret_key =         twiterkeys [1]
access_token =       twiterkeys [2]
accessSecret_token = twiterkeys [3]
print("\n>> Leitura das keys completa")
print('Api:          ', api_key)
print('Secret Key:   ', secret_key)
print('Access Token: ', access_token)
print('Secret Access Token: ', accessSecret_token)
#no terminal funciona mas no vscode nao (????)

aunthenticator = tweepy.OAuthHandler(api_key, secret_key)
aunthenticator.set_access_token(access_token, accessSecret_token)

api = tweepy.API(aunthenticator, wait_on_rate_limit=True)

dogecoin = 'Dogecoin'
search = f'#{dogecoin}'