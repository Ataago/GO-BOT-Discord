# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
import os
import datetime
import roles

class admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    async def get_file_data(self, server, fileName):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)  #GO-BOT-DISCORD
        currentdir += "\\data\\settings\\"
                
        file_data = currentdir + server.name + "_" + server.id + "//" + fileName

        if os.path.isfile(file_data):
            with open(file_data) as file_data:
                return discord.utils.get(server.channels, id = file_data.read())
                
        else:
            return None

    async def on_voice_state_update(self, before, after):
        CurTime = datetime.datetime.now()
        log_channel = await self.get_file_data(before.server, 'log_channel')

        if before.voice_channel.name == after.voice_channel.name:
            return
            
        if not log_channel:
            return  #server doesnt have log channel assigned
        
        try:
            before_channel = before.voice_channel.name
            after_channel = after.voice_channel.name
            #print('{} has changed from {} to {}'.format(before.name, before_channel, after_channel))
            embed = discord.Embed(
                    title = '🔄 ' + before.name  ,
                    description = 'switched from 🔊 **' + before_channel + '** to  🔊 **' + after_channel + '**',
                    colour = discord.Color.orange()
                )
            embed.set_footer(text = 'Voice switch: ' + CurTime.strftime("%I:%M:%S %p") + ' IST')
            await self.GoBot.send_message(log_channel, embed = embed)
        except:
            pass
        
        try:
            before_channel = before.voice_channel.name
        except:
            after_channel = after.voice_channel.name
            #print('{} has joinned {}'.format(after.name, after_channel))
            embed = discord.Embed(
                    title = '✔️  ' + after.name ,
                    description = 'joined 🔊 **' + after_channel + '**',
                    colour = discord.Color.green()
                )
            embed.set_footer(text = 'Voice join: ' + CurTime.strftime("%I:%M:%S %p") + " IST ")
            await self.GoBot.send_message(log_channel, embed = embed)
        
        try:
            after_channel = after.voice_channel.name
        except:
            before_channel = before.voice_channel.name
            #print('{} has left {}'.format(before.name, before_channel))
            embed = discord.Embed(
                    title = '❌  ' + after.name ,
                    description = 'left 🔊  **' + before_channel + '**',
                    colour = discord.Color.red()
                )
            embed.set_footer(text = 'Voice leave: ' + CurTime.strftime("%I:%M:%S %p") + ' IST')
            await self.GoBot.send_message(log_channel, embed = embed)
            

def setup(GoBot):
    GoBot.add_cog(admin(GoBot))