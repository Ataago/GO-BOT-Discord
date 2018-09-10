# @file The starting point of the GO BOT
# @author Ataago 
# @license GPL-3.0
 

import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import os

os.chdir(r'E:\Git\GO-BOT-Discord\commands')
extensions = []
for dirpath, dirnames, filenames in os.walk('E:\Git\GO-BOT-Discord\commands'):
    if dirpath == 'E:\Git\GO-BOT-Discord\commands':
        for file in filenames:
            extensions.append(os.path.splitext(file)[0])   
print('Modules Detected: ',extensions)

GoBot = commands.Bot(command_prefix = 'go ')
#GoBot.remove_command('help')

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
    print('\nGO BOT is Ready to GO!\n')

@GoBot.event
async def on_message(message):
    print('{} in {}-{}: {}'.format(message.author,message.channel,message.server, message.content))
    await GoBot.process_commands(message)

if __name__ == '__main__':
    for extension in extensions:
        try:
            GoBot.load_extension(extension)
            #print('Loaded: ',extension)
        except Exception as error:
            GoBot.unload_extension(extension)
            print('\nCould not load: ',extension)
            print(error)

    try:
        #TOKEN = input("\nEnter GO TOKEN: ")
        TOKEN = 'NDg3NjMwNjU3MDI4MzU4MTQ1.DneRMQ.ewrkApicUfAme6FK_N7sRL-3CVQ'
        GoBot.loop.create_task(change_status()) #change status
        GoBot.run(TOKEN)    #run the bot
        
    except discord.errors.LoginFailure as e:
        print(e)
        input()