# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
import os
import roles

class admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    async def get_file_data(self, server, fileName):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)  #GO-BOT-DISCORD
        currentdir += "\\data\\settings\\"
                
        file_data = currentdir + server.name + "_" + server.id + "//" + fileName

        if os.path.isfile(file_data):
            with open(file_data) as file_data:
                return file_data.read()
        else:
            return None

    async def get_role_id(self, server, roleName):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)  #GO-BOT-DISCORD
        currentdir += "\\data\\settings\\"
                
        autorole_file = currentdir + server.name + "_" + server.id + "//" + roleName

        if os.path.isfile(autorole_file):
            with open(autorole_file) as autorole_file:
                return discord.utils.get(server.roles, id = autorole_file.read())
        else:
            return None
        
    @commands.command(pass_context = True)
    async def configs(self, ctx):
        server = ctx.message.server

        if not (await roles.Admin.check_role(self, ctx.message, 'adminrole')):
            await self.GoBot.say("You dont have Permissions")
            return


        adminrole = await self.get_file_data(server, 'adminrole')
        adminrole = discord.utils.get(server.roles, id = adminrole)  
        if not adminrole:
            adminrole = 'go set_admin_role'

        autorole = await self.get_file_data(server, 'autorole')
        autorole = discord.utils.get(ctx.message.server.roles, id = autorole)
        if not autorole:
            autorole =  'go autorole <role_name>'

        modrole = await self.get_file_data(server, 'modrole')
        modrole = discord.utils.get(server.roles, id = modrole) 
        if not modrole:
            modrole =  'go modrole <role_name>'

        log_channel = await self.get_file_data(server, 'log_channel')
        log_channel = discord.utils.get(server.channels, id = log_channel) 
        if not log_channel:
            log_channel =  'go set_log_channel <log_text_channel_name>'

        suggestion_channel = await self.get_file_data(server, 'suggestion_channel')
        suggestion_channel = discord.utils.get(server.channels, id = suggestion_channel) 
        if not suggestion_channel:
            suggestion_channel =  'go set_suggestions_channel <channel_name>'

        embed = discord.Embed(
                    title = ctx.message.server.name ,
                    description = 'Here you can find all the Configs for your server',
                    colour = discord.Color.dark_gold()
                )
        embed.set_thumbnail(url= server.icon_url)
        embed.add_field(name = 'Admin Role', value = adminrole, inline=False)
        embed.add_field(name = 'Auto Role', value = autorole, inline=False)
        embed.add_field(name = 'Moderator Role', value = modrole, inline=False)
        embed.add_field(name = 'Log Channel', value = log_channel, inline=False)
        embed.add_field(name = 'Suggestions Channel', value = suggestion_channel, inline=False)
        await self.GoBot.send_message(ctx.message.author, embed = embed)
        await self.GoBot.say('I have sent you a Personal Message!')
        '''try:
            title = ctx.message.content[11:].split('|')[0]
            suggestion = ctx.message.content[11:].split('|')[1]
        except:
            await self.GoBot.say("Enter a suggestion tile and its body ```go suggest suggestion_title | suggestion_body```")
            return

        suggestion_channel = await self.get_file_data(ctx.message.server, 'suggestion_channel')
        if not suggestion_channel:
            await self.GoBot.say("Suggestion channel is not Assigned. Contact your Admin.")
            return

        embed = discord.Embed(
                    title = title  ,
                    description = suggestion,
                    colour = discord.Color.dark_gold()
                )
        embed.set_author(name= user.name , icon_url = user.avatar_url)
        embed.set_footer(text = 'Suggestion from ' + user.name)
        await self.GoBot.send_message(suggestion_channel, embed = embed)
        await self.GoBot.say("{}'s suggestion posted in #{}".format(user.name, suggestion_channel))'''

def setup(GoBot):
    GoBot.add_cog(admin(GoBot))