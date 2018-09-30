# @author Ataago 
# @license GPL-3.0

#yet to be designed

import discord
from discord.ext import commands

class Info():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context = True)
    async def help(self, ctx):
        author = ctx.message.author #/channel/author
        
        embed = discord.Embed(
            title = 'HELP',
            description = 'Trigger a Command using "go "',
            colour = discord.Color.green()
        )

        #embed.set_author(name = 'Help')
        embed.set_author(name='GO BOT', icon_url ='https://media.discordapp.net/attachments/487643988858372096/487968875242192898/GO2.png')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/487643988858372096/488620105782263814/Help.png?width=683&height=683')
        embed.add_field(name = 'go about', value = 'Know about the Developers',inline=True)
        embed.add_field(name = 'go ping', value = 'Returns Pong!', inline=True)
        embed.add_field(name = 'go echo <statement>', value = 'Echos the statment', inline=True)
        embed.add_field(name = 'go clear <integer>', value = 'Deletes previous messages', inline=True)
        embed.add_field(name = 'go join', value = 'Joins your Voice Channel', inline=True)
        embed.add_field(name = 'go leave', value = 'Leaves your Voice Channel', inline=True)
        await self.GoBot.send_message(author,embed=embed)
        await self.GoBot.say('I have sent you a Personal Message!')
        
def setup(GoBot):
    GoBot.add_cog(Info(GoBot))