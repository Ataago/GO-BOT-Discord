# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands
import roles

class admin():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context=True)
    async def move(self, ctx):
        current_channel = ctx.message.author.voice.voice_channel

        to = ctx.message.content[0:].split(" ")[2]
        if to != 'to':
            await self.GoBot.say("Type 'move to <Voice_channel_name>'")
            return

        if not (await roles.Admin.check_role(self, ctx.message, 'adminrole')):
            await self.GoBot.say("You dont have Permissions")
            return

        channel = ctx.message.content[0:].split(" ")[3]
        destination_channel = discord.utils.get(ctx.message.server.channels, name=channel, type=discord.ChannelType.voice)
        if not destination_channel:
            await self.GoBot.say('Could not find voice channel: {}'.format(channel))

        try:
            members = current_channel.voice_members
            count = len(members)
        except:
            await self.GoBot.say('You need to be in Voice Channel')
            return

        while members:
            await self.GoBot.move_member(members[0], destination_channel)
            print('GO moved {} to {}'.format(members[0].name, destination_channel))
            del members[0]
        
        await self.GoBot.say("Moved {} members form {} to {}".format(count, current_channel, destination_channel))


def setup(GoBot):
    GoBot.add_cog(admin(GoBot))