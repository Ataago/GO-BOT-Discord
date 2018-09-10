# @author Ataago 
# @license GPL-3.0

#fix exception handling

import discord
from discord.ext import commands

class Mod():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    #echo line.
    @commands.command(pass_context = True)
    async def echo(self, ctx):
        try:
            await self.GoBot.say(ctx.message.content[8:])
        except discord.errors.HTTPException:
            await self.GoBot.say('What to echo? For example- "go echo hi"') 

    #echo mult - line. bug
#    @commands.command(pass_str = True)
 #   async def echo(self, *args):
  #      display = ''
   #     try:
    #        for word in args:
     #           display += word
      #          display += ' '
       #     await self.GoBot.say(display)
#
 #       except discord.errors.HTTPException:
  #          await self.GoBot.say('What to echo? For example- "go echo hi"') 

def setup(GoBot):
    GoBot.add_cog(Mod(GoBot))