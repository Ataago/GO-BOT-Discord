# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
from goInfo import Ataago

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command(pass_context = True)
    async def unload(self, ctx,  extension):
        if ctx.message.author.id == Ataago.ID:
            try:
                self.GoBot.unload_extension(extension)
                print('Unloaded {}'.format(extension))
                await self.GoBot.send_message(ctx.message.author,'Unloaded: %s'% extension )

            except Exception as error:
                print(error)

def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))