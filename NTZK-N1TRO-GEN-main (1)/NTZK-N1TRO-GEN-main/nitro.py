import os
import ctypes
import random
import requests

from time import sleep
from colorama import Fore
from discord_webhook import DiscordWebhook, DiscordEmbed

def fire(text):
    os.system(""); fade = ""
    green = 250
    for line in text.splitlines():
        fade += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return fade

def proxy():
    proxiess = input("Drag and drop your proxy file here: ")
    proxies = open(proxiess).read().split('\n')
    proxy = proxies[0]
    with open(proxiess, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return ({'http://': f'http://{proxy}', 'https://': f'https://{proxy}'})

def sendnitro(nitro,webhook_url):
    webhook = DiscordWebhook(url=webhook_url,username="Nitro-Gen", avatar_url="https://cdn.discordapp.com/attachments/961950134814535700/961986922136338493/unknown1.png")
    embed = DiscordEmbed(title='Nitro-Gen', description='🎉Congratulation You Found A Nitro🎉', color='03b2f8')
    embed.set_footer(text='Made By NTZK')
    embed.add_embed_field(name='✨Nitro✨', value='Click Claim To Caim You Nitro')
    embed.set_image(url="https://cdn.discordapp.com/attachments/961950134814535700/961986922136338493/unknown1.png")
    webhook.add_embed(embed)
    webhook2 = DiscordWebhook(url=webhook_url,username="Nitro-Gen", avatar_url="https://cdn.discordapp.com/attachments/961950134814535700/961986922136338493/unknown1.png", content=nitro)
    webhook.execute()
    webhook2.execute()

def TWISTX7():
    os.system("cls && title NITRO-GEN BY NTZK")
    generated = []
    valid = []
    invalid = []
    print(fire(f"""
   
   
                     ╔═════════════════════════════════════════════════════╗            
                     ║         ╔╗╔╔═╗═╗ ╦╦╦ ╦╔═╗  ╔╗╔╦╔╦╗╦═╗╔═╗            ║
                     ║         ║║║║ ║╔╩╦╝║║ ║╚═╗  ║║║║ ║ ╠╦╝║ ║            ║
                     ║         ╝╚╝╚═╝╩ ╚═╩╚═╝╚═╝  ╝╚╝╩ ╩ ╩╚═╚═╝            ║
                     ║                                                     ║
                     ║═════════════════════════════════════════════════════║
                     ║       Made By-! N T Z K#5083                        ║
                     ║       Discord: https://discord.gg/noixus            ║
                     ╚═════════════════════════════════════════════════════╝
                                                                                       

"""))

    nitro_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    length = 16
    webhook_url = input(f"{Fore.YELLOW}Pon tu  Webhook -> {Fore.RESET}")
    usr_proxy = input(f"{Fore.YELLOW}Quieres usar Proxis? (y/n) -> {Fore.RESET}")
    if usr_proxy == "y" or usr_proxy == "Y":
        proxiess = input(f"{Fore.YELLOW}arastra el Archivo de las proxis aquí! -> {Fore.RESET}")
        def proxy():
            proxies = open(proxiess).read().split('\n')
            proxy = proxies[0]
            with open(proxiess, 'r+') as fp:
                lines = fp.readlines()
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])
            return ({'http://': f'http://{proxy}', 'https://': f'https://{proxy}'})
        amount = input(f"{Fore.YELLOW}Cuantos Discord Nitros quieres generar? ) -> {Fore.RESET}")
        if amount == "X" or amount == "x":
            try:
                while True:
                    password = "".join(random.sample(nitro_string, length))
                    nitro = "https://discord.gift/" + password
                    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
                    r = requests.get(url,proxies=proxy())
                    if r.status_code == 200:
                        print(f"{Fore.GREEN}Valid |{Fore.RESET} {nitro} | {r.status_code}")
                        sendnitro(nitro,webhook_url)
                        valid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("Valid " + str(len(valid)) + "Invalid " + str(len(invalid)))
                    elif r.status_code == 429:
                        print(f"{Fore.YELLOW}Too Many Requests |{Fore.RESET} {nitro} | {r.status_code}")
                    else:
                        print(f"{Fore.RED}Invalid |{Fore.RESET} {nitro} | {r.status_code}")
                        invalid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("NITRO-GEN BY NTZK | Valido -> " + str(len(valid)) + " | Invalido -> " + str(len(invalid)))
            except KeyboardInterrupt:
                    result = input("Quieres jugar los Resultados? (y/n)")
                    if result == "y" or result == "Y":
                        print("")
                        print("Results:")
                        print("")
                        print(f"{Fore.YELLOW}Generated {Fore.RESET}-> {len(generated)}")
                        print(f"{Fore.RED}Invalid {Fore.RESET}-> {len(invalid)}")
                        print(f"{Fore.GREEN}Valid {Fore.RESET}-> {len(valid)}")
                        print("")
                        os.system("pause")
                        TWISTX7()
                    else:
                        TWISTX7()
        else:
            try:
                amount = int(amount)
                for x in range(amount):
                    password = "".join(random.sample(nitro_string, length))
                    nitro = "https://discord.gift/" + password
                    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
                    r = requests.get(url,proxies=proxy())
                    if r.status_code == 200:
                        print(f"{Fore.GREEN}Valid |{Fore.RESET} {nitro} | {r.status_code}")
                        sendnitro(nitro,webhook_url)
                        valid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("NITRO-GEN BY NTZK | Valid -> " + str(len(valid)) + " | Invalid -> " + str(len(invalid)))
                    elif r.status_code == 429:
                        print(f"{Fore.YELLOW}Too Many Requests |{Fore.RESET} {nitro} | {r.status_code}")
                        generated.append(nitro)
                    else:
                        print(f"{Fore.RED}Invalid |{Fore.RESET} {nitro} | {r.status_code}")
                        invalid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("NITRO-GEN BY NTZK | Valid -> " + str(len(valid)) + " | Invalid -> " + str(len(invalid)))
                print("")
                print("Results:")
                print("")
                print(f"{Fore.YELLOW}Generated {Fore.RESET}-> {len(generated)}")
                print(f"{Fore.RED}Invalid {Fore.RESET}-> {len(invalid)}")
                print(f"{Fore.GREEN}Valid {Fore.RESET}-> {len(valid)}")
                print("")
                os.system("pause")
                TWISTX7()
            except KeyboardInterrupt:
                    result = input("Do You Want To See The Result (y/n)")
                    if result == "y" or result == "Y":
                        print("")
                        print("Results:")
                        print("")
                        print(f"{Fore.YELLOW}Generated {Fore.RESET}-> {len(generated)}")
                        print(f"{Fore.RED}Invalid {Fore.RESET}-> {len(invalid)}")
                        print(f"{Fore.GREEN}Valid {Fore.RESET}-> {len(valid)}")
                        print("")
                        os.system("pause")
                        TWISTX7()
                    else:
                        TWISTX7()
    elif usr_proxy == "n" or usr_proxy == "N":
        amount = input(f"{Fore.YELLOW}How Many Discord Nitro You Want (X For Endless Mode ) -> {Fore.RESET}")
        if amount == "X" or amount == "x":
            while True:
                try:
                    password = "".join(random.sample(nitro_string, length))
                    nitro = "https://discord.gift/" + password
                    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f"{Fore.GREEN}Valid |{Fore.RESET} {nitro} | {r.status_code}")
                        sendnitro(nitro,webhook_url)
                        valid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("Valid " + str(len(valid)) + "Invallid " + str(len(invalid)))
                    elif r.status_code == 429:
                        print(f"{Fore.YELLOW}Too Many Requests |{Fore.RESET} {nitro} | {r.status_code}")
                        generated.append(nitro)
                    else:
                        print(f"{Fore.RED}Invalid |{Fore.RESET} {nitro} | {r.status_code}")
                        invalid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("NITRO-GEN BY TWISTX7#9122 | Valid -> " + str(len(valid)) + " | Invalid -> " + str(len(invalid)))
                except KeyboardInterrupt:
                    result = input("Do You Want To See The Result (y/n)")
                    if result == "y" or result == "Y":
                        print("")
                        print("Results:")
                        print("")
                        print(f"{Fore.YELLOW}Generated {Fore.RESET}-> {len(generated)}")
                        print(f"{Fore.RED}Invalid {Fore.RESET}-> {len(invalid)}")
                        print(f"{Fore.GREEN}Valid {Fore.RESET}-> {len(valid)}")
                        print("")
                        os.system("pause")
                        TWISTX7()
                    else:
                        TWISTX7()
        else:
            try:  
                amount = int(amount)
                for x in range(amount):
                    password = "".join(random.sample(nitro_string, length))
                    nitro = "https://discord.gift/" + password
                    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f"{Fore.GREEN}Valid |{Fore.RESET} {nitro} | {r.status_code}")
                        sendnitro(nitro,webhook_url)
                        valid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("NITRO-GEN BY NTZK| Valid -> " + str(len(valid)) + " | Invalid -> " + str(len(invalid)))
                    elif r.status_code == 429:
                        print(f"{Fore.YELLOW}Too Many Requests |{Fore.RESET} {nitro} | {r.status_code}")
                        generated.append(nitro)
                    else:
                        print(f"{Fore.RED}Invalid |{Fore.RESET} {nitro} | {r.status_code}")
                        invalid.append(nitro)
                        generated.append(nitro)
                        ctypes.windll.kernel32.SetConsoleTitleW("NITRO-GEN BY NTZK | Valid -> " + str(len(valid)) + " | Invalid -> " + str(len(invalid)))
                print("")
                print("Results:")
                print("")
                print(f"{Fore.YELLOW}Generated {Fore.RESET}-> {len(generated)}")
                print(f"{Fore.RED}Invalid {Fore.RESET}-> {len(invalid)}")
                print(f"{Fore.GREEN}Valid {Fore.RESET}-> {len(valid)}")
                print("")
                os.system("pause")
                TWISTX7()
            except KeyboardInterrupt:
                    result = input("Quieres guardar los Resultados¿? (y/n)")
                    if result == "y" or result == "Y":
                        print("")
                        print("Results:")
                        print("")
                        print(f"{Fore.YELLOW}Generated {Fore.RESET}-> {len(generated)}")
                        print(f"{Fore.RED}Invalid {Fore.RESET}-> {len(invalid)}")
                        print(f"{Fore.GREEN}Valid {Fore.RESET}-> {len(valid)}")
                        print("")
                        os.system("pause")
                        TWISTX7()
                    else:
                        TWISTX7()
    else:
        print(f"{Fore.RED}Invalid Choice {Fore.RESET}")
        sleep(1)
        TWISTX7()
        
        
TWISTX7()
