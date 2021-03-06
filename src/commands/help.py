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
        embed.set_author(name='GO BOT', icon_url ='https://cdn.discordapp.com/attachments/487643988858372096/487967609577537537/GO.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/487643988858372096/498871497868443648/Help.png')
    
        embed.add_field(name = 'Fun Commands', value = '`allo` `gn` `gm` `die` `allo` `echo`', inline=False)
        embed.add_field(name = 'Information commands', value = '`about` `help` `rank @user_name`',inline=False)
        embed.add_field(name = 'Music commands', value = '`join` `leave` `play <url/name>` `queue <url/name>` `next` `pause` `resume` `stop`', inline = False)
        embed.add_field(name = 'Action commands', value = '`vote <option_no>` `suggest suggestion_title | suggestion_body` ',inline=False)
        embed.add_field(name = 'Moderator commands', value = '`clear <number>` `xp @name <expValue>` `vote start` `vote end`', inline = False)
        embed.add_field(name = 'Admin commands', value = '`move to <channel_name>` `configs` ', inline = False)
        embed.add_field(name = 'GO Bot Setup', value = '`setup` make sure to have an Admin role named `admin`', inline = False)
    



  
 
        '''embed.add_field(name = 'FUN', value = '``allo`` `gn` `die` ', inline=False)
        embed.add_field(name = 'go about', value = 'Know about the Developers',inline=False)
        #embed.add_field(name = 'go allo', value = 'Returns Pong!', inline=True)
        embed.add_field(name = 'go echo <statement>', value = 'Echos the statment', inline=False)
        embed.add_field(name = 'go suggest suggestion_title | suggestion_body ', value = 'Suggest something in the server', inline=False)
        embed.add_field(name = 'go rank @name', value = 'Rank of the player', inline=False)
        embed.add_field(name = 'go clear <integer>', value = 'Deletes previous messages. Permission: admin, modrole', inline=False)
        embed.add_field(name = 'go join', value = 'Joins your VC', inline=False)
        embed.add_field(name = 'go leave', value = 'Kick GO from VC', inline=False)
        embed.add_field(name = 'go play <url/name>', value = 'Plays audio from youtube video', inline=False)
        embed.add_field(name = 'go queue <url/name>', value = 'Adds song to play next in queue', inline=False)
        embed.add_field(name = 'go next', value = 'Skip song', inline=False)
        embed.add_field(name = 'go pause', value = 'Pause now playing', inline=False)
        embed.add_field(name = 'go resume', value = 'Resume song', inline=False)
        embed.add_field(name = 'go stop', value = 'Stop playing', inline=False)
        embed.add_field(name = 'go xp @name <expValue>', value = 'Increase or Decrease @name xp. Permissions: adminrole, modrole', inline=False)
        embed.add_field(name = 'go move to <channel_name>', value = 'move all users to chanel_name', inline=False)
        embed.add_field(name = 'go set_admin_role', value = 'Create an Admin role named `admin`', inline = False)
        embed.add_field(name = 'go configs', value = 'Check all the configs. remember to run `go set_admin_role`', inline = False)'''

        embed.set_footer(text = 'DM Ataago on Discord - #8094')
        await self.GoBot.send_message(author,embed=embed)
        await self.GoBot.say('I have sent you a Personal Message!')
        
def setup(GoBot):
    GoBot.add_cog(Info(GoBot))