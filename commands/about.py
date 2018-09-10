import discord
from discord.ext import commands

class Info():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command()
    async def about(self):
        embed = discord.Embed(
            title = 'GO BOT',
            description = 'Go is under Development. Stay tuned and give suggestions.',
            color = discord.Color.green()
        )

        #embed.set_image(url ='https://media.discordapp.net/attachments/487643988858372096/487963343676506132/unknown.png')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/487643988858372096/487968875242192898/GO2.png')
        embed.set_author(name='Ataago - Owner', icon_url ='https://media.discordapp.net/attachments/487643988858372096/487963343676506132/unknown.png')
        embed.add_field(name='How to use GO BOT?',value = 'Just type in "go help" to start using the BOT.',inline=False)
        #embed.add_field(name='Field Name',value = 'Field value',inline=True)
        #embed.add_field(name='Field Name',value = 'Field value',inline=True)
        embed.set_footer(text = 'DM Ataago on Discord - #8094')

        await self.GoBot.say(embed=embed)

def setup(GoBot):
    GoBot.add_cog(Info(GoBot))
