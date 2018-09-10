# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command()
    async def unload(self, extension):
        try:
            self.GoBot.unload_extension(extension)
            print('Unloaded {}'.format(extension))

        except Exception as error:
            print(error)

def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))