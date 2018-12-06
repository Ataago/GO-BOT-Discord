# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
from goInfo import Ataago
import roles

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context = True)
    async def say(self, ctx):
        message = ctx.message
        prefix = message.content.split(" ")[0]
        invoke = message.content.split(" ")[1]

        messageStartsFrom = len(prefix) + len(invoke) + 1

        #check if user has xprole, import roles
        if not await roles.Admin.check_role(self, ctx.message, 'adminrole'):
            await self.GoBot.say("You dont have Permissions")
            return

        await self.GoBot.delete_message(message)
        await self.GoBot.say(message.content[messageStartsFrom : ])
        
def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))