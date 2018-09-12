# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class Test():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command(pass_context = True)
    async def allo(self,ctx):
        if ctx.permissions(administrator):
            print("is admin")
            await self.GoBot.say('Allo {}!!!!'.format(ctx.message.author.mention))
        else:
            print("not an admin")

def setup(GoBot):
    GoBot.add_cog(Test(GoBot))