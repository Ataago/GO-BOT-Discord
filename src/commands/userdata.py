# @author Ataago 
# @license GPL-3.0

#make the currentdir as class variables

import discord
from discord.ext import commands
import os
import json
#import datetime

import roles

class Admin():
    #CurTime = datetime.datetime.now()

    def __init__(self, GoBot):
        self.GoBot = GoBot

    async def check_server(self, server_name):
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)
        currentdir += "\\data\\userExp"

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
        currentdir = os.path.dirname(currentdir)  #GO-BOT-DISCORD
        currentdir += "\\data\\userExp"
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
        currentdir += "\\data\\userExp"
        os.chdir(currentdir)

        """spam_time = 10

        time_now = datetime.datetime.now()
        time_now_H = int(time_now.strftime('%H'))*60*60
        time_now_M = int(time_now.strftime('%M'))*60
        time_now_S = int(time_now.strftime('%S'))
        CurTime_H = int(self.CurTime.strftime('%H'))*60*60
        CurTime_M = int(self.CurTime.strftime('%M'))*60
        CurTime_S = int(self.CurTime.strftime('%S'))
        print(time_now_S,CurTime_S)
        if abs( (CurTime_H + CurTime_M + CurTime_S) - (time_now_H + time_now_M + time_now_S) ) < spam_time:
            return"""

        if message.author.id == '487630657028358145' or message.author.id == '498773725534093332': #GO BOT messages ignored
            return
        #self.CurTime = datetime.datetime.now()
        #print('This is not printed', message.author.id)                         #remove this line
        #handling DM to bot
        try:
            server_name = message.server.name
        except:
            name = await self.GoBot.get_user_info(message.author.id)
            print("{} texted the bot".format(message.author))
            await self.GoBot.send_message(name,"Don't try to make up conversation. \n:joy: :joy: :joy: :joy: :joy: :joy: :joy: ")
            return

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
        if users[user.name]['experience'] < 0:
            users[user.name]['experience'] = 0

    async def level_up(self, users, user, channel):
        experience = users[user.name]['experience']
        lvl_start = users[user.name]['level']
        lvl_end = int(experience ** (1/4))
    
        if lvl_start < lvl_end:
            await self.GoBot.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
            users[user.name]['level'] = lvl_end

    
    @commands.command(pass_context = True)
    async def rank(self, ctx, user: discord.Member):
        """'go rank @name'"""
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)
        currentdir += "\\data\\userExp"
        os.chdir(currentdir)

        user_name = str(user.name) 
        user_avatar = str(user.avatar_url)
        server_name = ctx.message.server.name
        user_xp = {}
        rank = 0

        file_name = await self.check_server(server_name)
        with open(file_name,'r') as f:
            users = json.load(f)

        for user in users:
            user_xp[user] = users[user]['experience']

        user_rank = sorted(user_xp.items(), key = lambda user_xp: user_xp[1], reverse = True)

        for user in user_rank:
            rank += 1

            #user[0] returns the name aka. first element of the tuple in a list
            if user_name == user[0]:

                embed = discord.Embed(
                    title = user_name + ' #' + str(rank),# + " in " + str(test_user.server.name),
                    description = 'in ' + str(server_name) ,#+ "'s rank in " + str(test_user.server.name)  ,
                    #description = 'Experience: ' + str(user[1]) + "\tLevel: "  + str(users[user[0]]['level']) ,
                    colour = discord.Color.green()
                )
                #embed.set_author(name=test_user.name)
                embed.set_thumbnail(url=user_avatar)
                embed.add_field(name = 'Level', value = str(users[user[0]]['level']), inline=True)
                embed.add_field(name = 'Experience', value = str(user[1]), inline=True)
                embed.set_footer(text = 'Requested by ' + ctx.message.author.name)
                await self.GoBot.say(embed = embed)

    @commands.command(pass_context = True)
    async def xp(self, ctx, user: discord.Member):
        """'go xp @name xpValue' xp value could be postive or negative"""
        currentdir = os.path.dirname(os.path.realpath(__file__)) 
        currentdir = os.path.dirname(currentdir)
        currentdir = os.path.dirname(currentdir)
        currentdir += "\\data\\userExp"
        os.chdir(currentdir)

        xp_limits = 200

        #check if user has xprole, import roles
        if not (await roles.Admin.check_role(self, ctx.message, 'adminrole') or await roles.Admin.check_role(self, ctx.message, 'moderole')):
            await self.GoBot.say("You dont have Permissions")
            return
            
        try:
            exp = int(ctx.message.content[0:].split(" ")[3])
            if exp > xp_limits or exp < -xp_limits:
                await self.GoBot.say("xp range: [-{}, {}]".format(xp_limits,xp_limits))
                return
        except:
            await self.GoBot.say("Enter: 'go xp @name -10' ")
            return

        server_name = ctx.message.server.name
        file_name = await self.check_server(server_name)

        with open(file_name,'r') as f:
            users = json.load(f)

        await self.add_experience(users, user, exp)
        await self.GoBot.say("{} xp: {}".format(exp,user.name))

        with open(file_name,'w') as f:
            json.dump(users, f)
 

def setup(GoBot):
    GoBot.add_cog(Admin(GoBot))