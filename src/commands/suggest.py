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

    @commands.command(pass_context = True)
    async def suggest(self, ctx):
        user = ctx.message.author

        try:
            title = ctx.message.content[11:].split('| ')[0]
            suggestion = ctx.message.content[11:].split('| ')[1]
        except:
            await self.GoBot.say("Enter a suggestion tile and its body ```go suggest suggestion_title | suggestion_body```")
            return

        print(title)
        print(suggestion)

        suggestion_channel = await self.get_file_data(ctx.message.server, 'suggestion_channel')
        print(suggestion_channel)

        if not suggestion_channel:
            await self.GoBot.say("Suggestion channel is not Assigned. Contact your Admin.")
            return

        embed = discord.Embed(
                    title = title  ,
                    description = suggestion,
                    colour = discord.Color.dark_gold()
                )
        embed.set_author(name= user.name , icon_url = user.avatar_url)
        embed.set_footer(text = 'Suggestion from ' + user.name)
        await self.GoBot.send_message(suggestion_channel, embed = embed)
        await self.GoBot.say("{}'s suggestion posted in #{}".format(user.name, suggestion_channel))

def setup(GoBot):
    GoBot.add_cog(admin(GoBot))