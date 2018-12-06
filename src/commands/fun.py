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

    @commands.command(pass_context = True)
    async def die(self,ctx):
        try:
            tag = ctx.message.content[0:].split(" ")[2]
            print(tag)
            if tag == '<@260089708300861452>':
                await self.GoBot.say('I am loyal unlike you.')
            elif  tag == '<@487630657028358145>':
                await self.GoBot.say("LOL, I am immortal {}!".format(ctx.message.author.mention))
            else:
                await self.GoBot.say("Merryweather strike team is dispatched for {}!  :gun: :bomb:".format(tag))

        except:
            await self.GoBot.say("LOL, I am immortal {}!".format(ctx.message.author.mention))

    @commands.command(pass_context = True)
    async def wink(self, ctx):
        await self.GoBot.say(':wink:')

    @commands.command(pass_context = True)
    async def DM(self, ctx):
        tag = ctx.message.content[0:].split(" ")[2]
        print(tag)
        reciever = '260089708300861452'
        name = self.GoBot.get_user_info(reciever)
        print(name)
        await self.GoBot.send_message(name,"hello noob" )

def setup(GoBot):
    GoBot.add_cog(Fun(GoBot))