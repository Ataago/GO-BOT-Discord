# @file The starting point of the GO BOT
# @author Ataago 
# @license GPL-3.0
 

import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import os
import time
import datetime

from commands.goInfo import Ataago
from commands.goInfo import key

#TOKEN = input("\nEnter GO TOKEN: ")
CurTime = datetime.datetime.now()
Time_of_disconnection = CurTime

gotrigger = 'go '
extensions = []
botcommands = ['allo', 'echo', 'clear', 'play', 'autorole', 'leave', 'help', 'pause','resume', 'join', 'stop', 'gn', 'die', 'about', 'queue', 'next', 'load', 'unload', 'say', 'wink', 'DM', 'rank', 'xp','modrole','set_admin_role','move', 'set_log_channel']
status_message = 'Beta Version 3.2'

currentdir = os.path.dirname(os.path.realpath(__file__))  + '\commands'
for dirpath, dirnames, filenames in os.walk(currentdir):
    if dirpath == currentdir:
        for file in filenames:
            extensions.append(os.path.splitext(file)[0])   
print('Modules Detected: ',extensions)

GoBot = commands.Bot(command_prefix = gotrigger)
GoBot.remove_command('help')

#Change status
status = ['Under Development', 'coming Soon!', 'type "go help"']
async def change_status():
    await GoBot.wait_until_ready()
    msgs = cycle(status)

    while not GoBot.is_closed:
        current_status = next(msgs)
        await GoBot.change_presence(game=discord.Game(name = current_status))
        await asyncio.sleep(2)

#on_ready
@GoBot.event
async def on_ready():
    owner = await GoBot.get_user_info(Ataago.ID)
    await GoBot.change_presence(game = discord.Game(name = status_message))  #Single status
    print('\nGO BOT is Ready to GO!\n\nRunning on:')
    print('________________________________________________________________________________________________\n')
    [(lambda server: print(" > %s (%s)"%(server.name, server.id))) (server) for server in GoBot.servers]
    print('________________________________________________________________________________________________\n')
    await GoBot.send_message(owner,'GO is Online now. \nBOT Was offline since: %s' % Time_of_disconnection.strftime("%d-%b-%Y  %I:%M:%S %p") )

@GoBot.command
async def logout():
    await GoBot.logout()
    print("Logout")
    input("hit enter to exit...")

@GoBot.event
async def on_message(message):
    CurTime = datetime.datetime.now()
    prefix = message.content[0:3]
    invoke = message.content[3:].split(" ")[0]

    print('{}: {} in {}-{}:\t{}'.format(CurTime.strftime("%Y-%m-%d %H:%M:%S"), message.author, message.channel, message.server, message.content))
    if invoke not in botcommands and prefix == gotrigger :
        await GoBot.send_message(message.channel,  embed = discord.Embed(color = discord.Color.red(), description = ("'%s' is not a GO command! \n\nEnter 'go help' " % invoke)))
        return
    await GoBot.process_commands(message)

if __name__ == '__main__':
    for extension in extensions:
        try:
            GoBot.load_extension(extension)
        except Exception as error:
            GoBot.unload_extension(extension)
            print('\nCould not load: ',extension)
            print(error)

    try:
        TOKEN = key.TOKEN
        print('\nIntializing Go...\n')

        while True:
            try:
                GoBot.loop.run_until_complete(GoBot.start(TOKEN))
            except BaseException:
                time_now = datetime.datetime.now()
                time_now_H = int(time_now.strftime('%H'))*60*60
                time_now_M = int(time_now.strftime('%M'))*60
                time_now_S = int(time_now.strftime('%S'))
                CurTime_H = int(CurTime.strftime('%H'))*60*60
                CurTime_M = int(CurTime.strftime('%M'))*60
                CurTime_S = int(CurTime.strftime('%S'))
                if abs( (CurTime_H + CurTime_M + CurTime_S) - (time_now_H + time_now_M + time_now_S) ) > 6:
                    Time_of_disconnection = datetime.datetime.now()
                CurTime = datetime.datetime.now()
                print('*********************************** {} No Network connection, Trying to Reconnect {} ***********************************'.format(CurTime.strftime('%H:%M:%S'), Time_of_disconnection.strftime('%H:%M:%S')))
                time.sleep(5)
        #GoBot.loop.create_task(change_status()) #change status with status list
        #GoBot.run(TOKEN)    #run the bot

    except discord.errors.LoginFailure as e:
        print(e)
        input('Hit Enter to exit.')