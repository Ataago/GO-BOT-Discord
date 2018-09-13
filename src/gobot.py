# @file The starting point of the GO BOT
# @author Ataago 
# @license GPL-3.0
 

import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import os
import key


#TOKEN = input("\nEnter GO TOKEN: ")

gotrigger = 'go '
extensions = []
botcommands = ['allo', 'echo', 'clear', 'play', 'autorole', 'leave', 'help', 'pause','resume', 'join', 'stop', 'gn', 'about', 'queue', 'next', 'load', 'unload', 'say']


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
    await GoBot.change_presence(game = discord.Game(name = 'Beta Version'))  #Single status
    print('\nGO BOT is Ready to GO!\n\nRunning on:')
    [(lambda server: print(" > %s (%s)"%(server.name, server.id))) (server) for server in GoBot.servers]

@GoBot.event
async def on_message(message):
    print('{} in {}-{}:\t{}'.format(message.author,message.channel,message.server, message.content))
    prefix = message.content[0:3]
    invoke = message.content[3:].split(" ")[0]
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

        #GoBot.loop.create_task(change_status()) #change status with status list
        GoBot.run(TOKEN)    #run the bot

    except discord.errors.LoginFailure as e:
        print(e)
        input('Hit Enter to exit.')