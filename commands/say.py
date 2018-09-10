import discord
from discord.ext import commands

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context = True)
    async def say(self, ctx):
        message = ctx.message
        await self.GoBot.delete_message(message)
        await self.GoBot.say(message.content[7:])
        
def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))