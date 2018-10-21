# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
import os
import json
import roles

class utility():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    currentdir = os.path.dirname(os.path.realpath(__file__)) 
    currentdir = os.path.dirname(currentdir)
    currentdir = os.path.dirname(currentdir)  #GO-BOT-DISCORD
    currentdir += "\\data\\server_data\\"

    async def create_json_file(self, server, fileName):
        if not os.path.isdir(self.currentdir + server.name + "_" + server.id ):
            os.makedirs(self.currentdir + server.name + "_" + server.id )

        data_file = self.currentdir + server.name + "_" + server.id + "//" + fileName
        if not os.path.isfile(data_file):
            data_file = open(data_file,"w")
            data_file.write("{}")
            data_file.close()

    async def save_file(self, server, fileName, data):
        '''updates the roleName file'''
        data_file = self.currentdir + server.name + "_" + server.id + "//" + fileName
        with open(data_file, "w") as data_file:
            json.dump(data, data_file)
    
    async def clear_file_data(self, server, fileName):
        data_file = self.currentdir + server.name + "_" + server.id + "//" + fileName
        if os.path.isfile(data_file):
            data_file = open(data_file,"w")
            data_file.write("{}")
            data_file.close()

    async def get_file_data(self, server, fileName):
        '''returns all data from the file'''
        data_file = self.currentdir + server.name + "_" + server.id + "//" + fileName

        if os.path.isfile(data_file):
            with open(data_file, 'r') as data_file:
                return json.load(data_file)
        else:
            return None

    async def display_poll(self, server, fileName, author_name, author_avatar, footer):
        vote_data = await self.get_file_data(server, fileName)
        option_list = vote_data['options']
        option_no = 1

        embed = discord.Embed(
            title = vote_data['Title'],
            description = vote_data['Description'],
            colour = discord.Color.green()
        )
        for option in option_list:
            name = '[' + str(option_no) + '] ' + option
            value = vote_data[str(option_no)]
            embed.add_field(name = name, value = 'Vote count: ' + str(value) , inline=False)
            option_no += 1
            
        embed.set_author(name = author_name, icon_url = author_avatar)
        embed.set_footer(text = footer)
        await self.GoBot.say(embed = embed)  

    @commands.command(pass_context = True)
    async def vote(self, ctx):
        print('line 1')

        server = ctx.message.server
        channel = ctx.message.channel
        fileName = 'poll_' + channel.id + '.json'
        voterLogFile = 'voters_' + channel.id + '.json'
        
        
        await self.create_json_file(server, fileName)
        await self.create_json_file(server, voterLogFile)
        vote_data = await self.get_file_data(server, fileName)
        voter_data = await self.get_file_data(server, voterLogFile)
        
        try:
            action = ctx.message.content[0:].split(" ")[2]
        except:
            print('go vote start/end/option')
            await self.GoBot.say('To use vote command enter ```go vote start/end/option```')
            return

        if action == 'start':
            if not (await roles.Admin.check_role(self, ctx.message, 'adminrole') or await roles.Admin.check_role(self, ctx.message, 'modrole')):
                await self.GoBot.say("You dont have Permissions")
                return
            try:
                if vote_data['Status'] == 'start':
                    print('vote aldready in progress')
                    await self.GoBot.say('Poll is aldready running in {}'.format(ctx.message.channel.name))
                    return
            except:
                print('File created for the first time')
                pass

            try:
                ctx.message.content[0:].split('|')[4]
            except:
                print('should have minimum 2 options to choose from with a title and description')
                print('go vote start | Title | Description | option 1 | option 2')
                await self.GoBot.say('Enter atleast 2 options with Title and Description of the Poll ```go vote start | Title | Description | option 1 | option 2```')
                return

            title = ctx.message.content[0:].split("|")[1]
            description = ctx.message.content[0:].split('|')[2]
            option_no = 1
            option_list = []

            await self.clear_file_data(server, fileName)
            await self.clear_file_data(server, voterLogFile)
            vote_data = await self.get_file_data(server, fileName)
            print('file cleared')

            vote_data['Status'] = 'start'
            vote_data['Admin'] = ctx.message.author.id
            vote_data['Title'] = title
            vote_data['Description'] = description

            for option in ctx.message.content[0:].split('|')[3:]:
                vote_data[option_no] = 0
                option_list.append(option)
                option_no += 1

            vote_data['options'] = option_list
            await self.save_file(server, fileName, vote_data)

            Admin = discord.utils.get(server.members, id = vote_data['Admin'])
            author_avatar = ctx.message.author.avatar_url
            footer = 'Poll created by ' + str(Admin)
            await self.display_poll(server, fileName, Admin, author_avatar, footer)

            print('Vote has started')
            print('Data in .json file',vote_data)
        
        if action == 'end':
            if vote_data['Admin'] != ctx.message.author.id:
                print('You have not started the poll')
                Admin = discord.utils.get(server.members, id = vote_data['Admin'])
                await self.GoBot.say('You are not authorized to end this Poll. Contact {}'.format(Admin))
                return

            try:
                if vote_data['Status'] == 'end':
                    print('no vote in progress in this channel')
                    await self.GoBot.say('No active poll in {}'.format(ctx.message.channel.name))
                    return
            except:
                print('no vote in progress in this channel in exception')
                await self.GoBot.say('No active poll in {}'.format(ctx.message.channel.name))
                return
            
            vote_data['Status'] = 'end'
            await self.save_file(server, fileName, vote_data)

            Admin = discord.utils.get(server.members, id = vote_data['Admin'])
            author_avatar = ctx.message.author.avatar_url
            footer = 'Poll has been ended by ' + str(Admin)
            await self.display_poll(server, fileName, Admin, author_avatar, footer)

            voter_data = await self.get_file_data(server, voterLogFile)

            embed = discord.Embed(
                title = 'Voters Participated',
                description = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ',
                colour = discord.Color.orange()
            )
            for voter in voter_data:
                name = discord.utils.get(server.members, id = voter)
                value = voter_data[voter]
                embed.add_field(name = name, value = 'Selected: ' + str(value) , inline=False)

                
            #embed.set_author(name = author_name, icon_url = author_avatar)
            #embed.set_footer(text = footer)
            await self.GoBot.say(embed = embed)  
            print('vote has ended')

        if action.isdigit():
            voter = ctx.message.author.id
            try:
                if vote_data['Status'] == 'end':
                    print('no vote in progress in this channel')
                    await self.GoBot.say('No active poll in {}'.format(ctx.message.channel.name))
                    return
            except:
                print('no vote in progress')
                await self.GoBot.say('No active poll in {}'.format(ctx.message.channel.name))
                return

            option_list = vote_data['options']
            if int(action) > len(option_list) or int(action) < 1:
                print('invalid option number, should range from 1 to {}'.format(len(option_list)))
                await self.GoBot.say('Option should range from 1 to {}'.format(len(option_list)))
                return

            print('vote call')
            print('voted for:',action)
            try:
                if voter_data[voter]:
                    print('aldready voted')
                    previous_vote = voter_data[voter]

                    count = vote_data[previous_vote]
                    vote_data[previous_vote] = count-1
                    await self.save_file(server, fileName, vote_data)

                    print('Vote changed')
                    await self.GoBot.say('{} has changed vote'.format(ctx.message.author.name))

            except:
                print('New voter')

            voter_data[voter] = action
            await self.save_file(server, voterLogFile, voter_data)

            count = vote_data[action]
            vote_data[action] = count+1
            await self.save_file(server, fileName, vote_data)

            author_name = ctx.message.author.name
            author_avatar = ctx.message.author.avatar_url
            footer = ctx.message.author.name + ' selected option -> ' + str(action)
            await self.display_poll(server, fileName, author_name, author_avatar, footer)
            print(voter_data) #to be   

        if action != 'start' and action != 'end' and not action.isdigit():
            print('go vote start | Title | Description | option 1 | option 2')
            await self.GoBot.say('To use vote command enter ```go vote start/end/option```')
            

def setup(GoBot):
    GoBot.add_cog(utility(GoBot))