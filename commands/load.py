import discord
from discord.ext import commands

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    @commands.command()
    async def load(self, extension):
        try:
            self.GoBot.load_extension(extension)
            print('Loaded {}'.format(extension))

        except Exception as error:
            print(error)


def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))