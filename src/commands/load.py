# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
from goInfo import Ataago

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command(pass_context = True)
    async def load(self, ctx, extension):
        if ctx.message.author.id == Ataago.ID:
            try:
                self.GoBot.load_extension(extension)
                print('Loaded {}'.format(extension))
                await self.GoBot.send_message(ctx.message.author,'Loaded: %s'% extension )

            except Exception as error:
                print(error)


def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))