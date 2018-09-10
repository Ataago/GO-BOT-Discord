# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class YT():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.GoBot.voice_client_in(server)
        try:
            await voice_client.disconnect()
        except:
            await self.GoBot.say('GO is not in any Voice Channel. Enter "go join".')


    
def setup(GoBot):
    GoBot.add_cog(YT(GoBot))