# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class Fun():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command(pass_context = True)
    async def gn(self,ctx):
        try:
            tag = ctx.message.content[0:].split(" ")[2]
            await self.GoBot.say("See you again {}!".format(tag))

        except:
            await self.GoBot.say("See you again {}!".format(ctx.message.author.mention))


def setup(GoBot):
    GoBot.add_cog(Fun(GoBot))