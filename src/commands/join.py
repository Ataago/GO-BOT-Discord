# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class YT():
    def __init__(self, GoBot):
        self.GoBot = GoBot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        server = ctx.message.server
        voice_client = self.GoBot.voice_client_in(server)

        try:
            try:
                if voice_client.is_connected():
                    await self.GoBot.say('Already in {} :loud_sound:  '.format(voice_client.channel))
                    return
            except: 
                pass
            await self.GoBot.join_voice_channel(channel)
        except:
            await self.GoBot.say('You must be in a Voice Channel.')

def setup(GoBot):
    GoBot.add_cog(YT(GoBot))