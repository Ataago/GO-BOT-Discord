#fix exception handling


import discord
from discord.ext import commands

class Mod():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    #Clear <number of lines>
    @commands.command(pass_context = True)
    async def clear(self, ctx, amount = 1):
        channel = ctx.message.channel
        todelete = []
        counter = -1
    
        try:
            async for message in self.GoBot.logs_from(channel, limit=int(amount+1)):
                todelete.append(message)
                counter += 1
            await self.GoBot.delete_messages(todelete)
            
            if counter != 1:
                await self.GoBot.say('{} Messages were cleared by {}!'.format(counter, ctx.message.author.name))
            else:
                await self.GoBot.say('{} Message was cleared by {}!'.format(counter, ctx.message.author.name))

        except discord.ext.commands.errors.BadArgument:
            await self.GoBot.say('Enter an interger value after go clear')
        except discord.ext.commands.errors.CommandInvokeError:
            await self.GoBot.say('type, go clear x, where x = [1,100]')
        
       # except: 
          #  await self.GoBot.say('Please enter an integer')


def setup(GoBot):
    GoBot.add_cog(Mod(GoBot))