# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
import os
import json

class Admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    async def check_server(self, server_name):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)
        currentdir += "\\data"

        file_name = server_name + ".json"
        creatfile = currentdir + "\\" + file_name

        server_list = []

        for dirpath, dirnames, filenames in os.walk(currentdir):
            if dirpath == currentdir:
                for file in filenames:
                    server_list.append(os.path.splitext(file)[0])   


        if server_name not in server_list:
            f = open(creatfile,"w")
            f.write("{}")
            f.close
            print(server_name,'.json user log file created in: ',currentdir)

        return file_name

    
    async def on_member_join(self, member):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)
        currentdir += "\\data"
        os.chdir(currentdir)

        server_name = member.server.name
        file_name = await self.check_server(server_name)

        with open(file_name,'r') as f:
            users = json.load(f)

        await self.update_data(users,member)
        #code
        with open(file_name,'w') as f:
            json.dump(users, f)



    async def on_message(self, message):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)
        currentdir += "\\data"
        os.chdir(currentdir)

        server_name = message.server.name
        file_name = await self.check_server(server_name)

        with open(file_name,'r') as f:
            users = json.load(f)

        await self.update_data(users, message.author)
        await self.add_experience(users, message.author,5)
        await self.level_up(users,message.author,message.channel)

        with open(file_name,'w') as f:
            json.dump(users, f)

    async def update_data(self, users, user):
        if not user.name in users:
            users[user.name] = {}
            users[user.name]['experience'] = 0
            users[user.name]['level'] = 1

    async def add_experience(self, users, user, exp):
        users[user.name]['experience'] += exp

    async def level_up(self, users, user, channel):
        experience = users[user.name]['experience']
        lvl_start = users[user.name]['level']
        lvl_end = int(experience ** (1/4))
    
        if lvl_start < lvl_end:
            await self.GoBot.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
            users[user.name]['level'] = lvl_end


def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))