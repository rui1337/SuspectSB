import discord, asyncio
from os import system
import shutil
import subprocess
import socket, sys, discord, base64, mysql.connector, threading, requests
from tpblite import TPB
from sys import argv
import psutil
import logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
#import desse discord.gg/niggers

init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + ' #')

def logo():
    try:
        print(Fore.LIGHTRED_EX)
        msg = f"""

                                    __ 
   _______  ___________  ___  _____/ /_
  / ___/ / / / ___/ __ \/ _ \/ ___/ __/
 (__  ) /_/ (__  ) /_/ /  __/ /__/ /_  
/____/\__,_/____/ .___/\___/\___/\__/    \n
        """
        for l in msg:
            print(l, end="")

    except KeyboardInterrupt:
        sys.exit()

logo()

print(Fore.RESET)
print('  ')
print('{}╔═════ Commands ════════════════════════════════╗{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [1] feitan {} : (purges your msgs)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [2] giyu :{} (delets every dm u sent)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [3] zzz :{} (ask me for explain)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [4] away :{} (removes status)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [5] tomioka :{} (leaves all the groups ur in))'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}╚══════════════════════════════════════════════╝{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()

token = "ODA4NzE4NDkwNzQyODE2ODA5.YIhTAA.O4Y3JBZqNLDBcLxgWDbWxDf9OuY"

def murder(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("terror".center(width))
        print()
        print("[-] made by rui#1337 [-]".center(width))
        print("[-] Logged In As: {0} [-]".format(client.user).center(width))
        print("[-] Sometimes i ask myself, L or N? [-]".format(client.user).center(width))
        print()
    ui()
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == 'feitan':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'giyu':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

        if commands[0] == 'zzz':
                        msg = message.content.split("zzz", 1)
                        args = msg[1].split("http", 1)
                        name = args[0]
                        url = "http"+args[1]
                        await message.delete()
                        await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=name, url=url))
                        container = discord.Embed(title="terror", color=0xFF3633)
                        container.add_field(name="status:", value="**"+name+"**")
                        container.set_footer(text="//")
                        await channel.send(embed=container)

        if commands[0] == "away":
                await message.delete()
                await client.change_presence(status=discord.Status.dnd)
        
        if commands[0] == "clrgroups":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()

        if commands[0] == "tomioka":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()

client.run(token, bot=False)