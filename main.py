import requests, os, colorama, json, time, threading, random, fade
from colorama import Fore

os.system("cls")
os.system("title Vanity Sniper - Made By Team77")
vanity ="""
__     __          _ _           ____        _


████████╗███████╗░█████╗░███╗░░░███╗███████╗███████╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║╚════██║╚════██║
░░░██║░░░█████╗░░███████║██╔████╔██║░░░░██╔╝░░░░██╔╝
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║░░░██╔╝░░░░██╔╝░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║░░██╔╝░░░░██╔╝░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░░░╚═╝░░░
                                                                    
[1] prees 1
"""
fadervanity = fade.greenblue(vanity)
print(fadervanity)
choicererer = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}CHOICE YOUR NUMBER{Fore.WHITE}: ")
if choicererer=="01"or choicererer=="1":
    os.system("cls")
    vanity1 ="""

████████╗███████╗░█████╗░███╗░░░███╗███████╗███████╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║╚════██║╚════██║
░░░██║░░░█████╗░░███████║██╔████╔██║░░░░██╔╝░░░░██╔╝
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║░░░██╔╝░░░░██╔╝░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║░░██╔╝░░░░██╔╝░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░░░╚═╝░░░
                                                                    """
    fadervanity2 = fade.greenblue(vanity1)
    print(fadervanity2)
    howmuch = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}How Much Urls You Want To Snipe (MAX 15){Fore.WHITE}: ")
    if howmuch =="1":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}Sniping : {Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX} ・Congratulations Mr.ALi {Fore.LIGHTGREEN_EX} ・You Sniped A New Vanity {Fore.LIGHTCYAN_EX} ・lets Find A New Vanity !")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX} discord.gg/45!")