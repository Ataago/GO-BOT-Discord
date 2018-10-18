# @author Ataago 
# @license GPL-3.0
"""Role Hierarchy 
        +adminrole
        +modrole      
        +autorole                    """

import discord
from discord.ext import commands
import os

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    currentdir = os.path.dirname(os.path.realpath(__file__)) 
    currentdir = os.path.dirname(currentdir)
    currentdir = os.path.dirname(currentdir)  #GO-BOT-DISCORD
    currentdir += "\\data\\settings\\"

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

    async def save_file(self, roleName, roleID, server):
        '''creates/updates the roleName file'''
        if not os.path.isdir(self.currentdir + server.name + "_" + server.id ):
            os.makedirs(self.currentdir + server.name + "_" + server.id )

        with open(self.currentdir + server.name + "_" + server.id + "//" + roleName, "w") as role_file:
            role_file.write(roleID)
            role_file.close()

    async def check_role(self, message, test_role):
        """test_role: modrole, adminrole, autorole"""
        server = message.server
        test_role_name = str(await Admin.get_role_id(self, server, test_role))

        if test_role_name in [role.name for role in message.author.roles]:
            print('Permission granted')
            return True
        print('Access Denied')
        return False
    
    @commands.command(pass_context = True)
    async def set_admin_role(self, ctx):
        """Set Admin Role, Default: admin"""
        role_name = 'admin'
        file_name = 'adminrole'

        role = discord.utils.get(ctx.message.server.roles, name = role_name)

        if role == None:
            await self.GoBot.say("Make sure the server contains admin role named as 'admin'")
        else:
            await self.save_file(file_name, role.id, ctx.message.server)
            await self.GoBot.say("Successfully set Admin Role as: {}".format(role.name))

    @commands.command(pass_context = True)
    async def autorole(self, ctx):
        """Select Auto on member join Role"""
        message = ctx.message.content
        role_name = message.split(" ")[2]
        file_name = 'autorole'
        #check if the user is admin
        if not await self.check_role(ctx.message, 'adminrole'):
            await self.GoBot.say("You dont have Permissions")
            return

        role = discord.utils.get(ctx.message.server.roles, name = role_name)

        if role == None:
            await self.GoBot.say("Enter a valid role existing on this server!!")
        else:
            await self.save_file(file_name, role.id, ctx.message.server)
            await self.GoBot.say("Successfully set autorole as: {}".format(role.name))

    async def on_member_join(self, member):
        await self.GoBot.send_message(member, "Hey welcome to " + member.server.name)
        await self.GoBot.send_message(member, "I am GO BOT developed by @Ataago#8094")
        autorole = await self.get_role_id(member.server, 'autorole')
        if autorole != None:
            try:
                await self.GoBot.add_roles(member, autorole)
                await self.GoBot.send_message(member, "\nYou have been automatically assigned to " + autorole.name + " role")
            except discord.errors.Forbidden:
                await self.GoBot.send_message(member, "\nSorry, I have no permissions to automatically assign you " + autorole.name + " role")
    
    @commands.command(pass_context = True)
    async def modrole(self, ctx):
        """Select XP modifier Role"""
        message = ctx.message.content
        role_name = message.split(" ")[2]
        file_name = 'modrole'
        #check if the user is admin
        if not await self.check_role(ctx.message, 'adminrole'):
            await self.GoBot.say("You don't have Permissions")
            return

        role = discord.utils.get(ctx.message.server.roles, name = role_name)

        if role == None:
            await self.GoBot.say("Enter a valid role existing on this server!!")
        else:
            await self.save_file(file_name, role.id, ctx.message.server)
            await self.GoBot.say("Successfully set modrole as: {}".format(role.name))

    @commands.command(pass_context = True)
    async def set_log_channel(self, ctx):
        """Set a text channel for Bot logs"""
        message = ctx.message.content
        channel_name = message.split(" ")[2]
        file_name = 'log_channel'

        if not await self.check_role(ctx.message, 'adminrole'):
            await self.GoBot.say("You don't have Permissions")
            return

        channel = discord.utils.get(ctx.message.server.channels, name=channel_name, type=discord.ChannelType.text)
        print(channel.id)
        if not channel:
            await self.GoBot.say("Enter a valid Text Channel that exists on this server!!")
            return
        
        await self.save_file(file_name, channel.id, ctx.message.server)
        await self.GoBot.say("Successfully set Bot Log Channel as: {}".format(channel))

def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))