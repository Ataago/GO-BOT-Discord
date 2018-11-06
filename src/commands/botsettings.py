# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
from goInfo import Ataago

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    

    @commands.command(pass_context = True)
    async def logout(self, ctx):
        if ctx.message.author.id == Ataago.ID:
            print('logout intiated')
            await self.GoBot.logout()
            print("Loged out!")

        else:
            owner = await self.GoBot.get_user_info(Ataago.ID)    #owner id object
            await self.GoBot.send_message(owner,"%s tried to logout the BOT. CAUTION\n*********************************** CAUTION ***********************************"% (ctx.message.author.name) )

    @commands.command(pass_context = True)
    async def load(self, ctx, extension):
        if ctx.message.author.id == Ataago.ID:
            try:
                self.GoBot.load_extension(extension)
                print('Loaded {}'.format(extension))
                await self.GoBot.send_message(ctx.message.author,'Loaded: %s'% extension )

            except Exception as error:
                print(error)
        else:
            owner = await self.GoBot.get_user_info(Ataago.ID)    #owner id object
            await self.GoBot.send_message(owner,"%s tried to load the BOT. CAUTION\n*********************************** CAUTION ***********************************"% (ctx.message.author.name) )

    @commands.command(pass_context = True)
    async def unload(self, ctx,  extension):
        if ctx.message.author.id == Ataago.ID:
            try:
                self.GoBot.unload_extension(extension)
                print('Unloaded {}'.format(extension))
                await self.GoBot.send_message(ctx.message.author,'Unloaded: %s'% extension )

            except Exception as error:
                print(error)
        else:
            owner = await self.GoBot.get_user_info(Ataago.ID)    #owner id object
            await self.GoBot.send_message(owner,"%s tried to unload the BOT. \n*********************************** CAUTION ***********************************"% (ctx.message.author.name) )



def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))