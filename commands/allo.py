import discord
from discord.ext import commands

class Test():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command(pass_context = True)
    async def allo(self,ctx):
        await self.GoBot.say('Allo there {}'.format(ctx.message.author.mention))

def setup(GoBot):
    GoBot.add_cog(Test(GoBot))