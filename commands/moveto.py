# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class YT():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context = True)
    async def moveto(self, ctx, channel):
        server = ctx.message.server
        voice_client = self.GoBot.voice_client_in(server)
        print(channel)
        print(voice_client.channel)
    
        #await voice_client.move_to(channel)

def setup(GoBot):
    GoBot.add_cog(YT(GoBot))