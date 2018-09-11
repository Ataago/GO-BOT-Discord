# @author Ataago 
# @license GPL-3.0

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

    async def get_role_id(self, server):
        autorole_file = self.currentdir + server.name + "_" + server.id + "//autorole"

        if os.path.isfile(autorole_file):
            with open(autorole_file) as autorole_file:
                return discord.utils.get(server.roles, id = autorole_file.read())
        else:
            return None

    async def save_file(self, roleID, server):

        if not os.path.isdir(self.currentdir + server.name + "_" + server.id ):
            os.makedirs(self.currentdir + server.name + "_" + server.id )

        with open(self.currentdir + server.name + "_" + server.id + "//autorole", "w") as autorole_file:
            autorole_file.write(roleID)
            autorole_file.close()

    @commands.command(pass_context = True)
    async def autorole(self, ctx):
        message = ctx.message.content
        role_name = message.split(" ")[2]

        role = discord.utils.get(ctx.message.server.roles, name = role_name)

        if role == None:
            await self.GoBot.say("Enter a valid role existing on this server!!")
        else:
            await self.save_file(role.id, ctx.message.server)
            await self.GoBot.say("Successfully set autorole as: {}".format(role.name))

    async def on_member_join(self, member):
        await self.GoBot.send_message(member, "Hey welcome to " + member.server.name)
        await self.GoBot.send_message(member, "I am GO BOT developed by @Ataago#8094")
        autorole = await self.get_role_id(member.server)
        if autorole != None:
            try:
                await self.GoBot.add_roles(member, autorole)
                await self.GoBot.send_message(member, "\nYou have been automatically assigned to " + autorole.name + " role")
            except discord.errors.Forbidden:
                await self.GoBot.send_message(member, "\nSorry, I have no permissions to automatically assign you " + autorole.name + " role")
 
def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))