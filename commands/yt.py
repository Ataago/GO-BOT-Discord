# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class YT():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    players = {}
    queues = {}

    def check_queue(self, id):
        if YT.queues[id] != []:
            player = YT.queues[id].pop(0)
            YT.players[id] = player
            player.start()
            await self.GoBot.say('Playing {}'.format(player.title))
            await self.GoBot.say('Duration: {}  | :thumbsup:: {} | :thumbsup:: {}'.format(player.duration, player.likes, player.dislikes)) 

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        channel = ctx.message.author.voice.voice_channel
        server = ctx.message.server
        voice_client = self.GoBot.voice_client_in(server)
        serverID = ctx.message.server.id
       
        try:
            if voice_client.is_connected():
                pass
            if YT.players[serverID].is_playing():
                YT.players[serverID].stop()
                
        except:
            await self.GoBot.join_voice_channel(channel)
            voice_client = self.GoBot.voice_client_in(server)
    
        player = await voice_client.create_ytdl_player(url, after=lambda: self.check_queue(server.id))
        YT.players[server.id] = player
        player.start()
        await self.GoBot.say('Playing {}'.format(player.title))
        await self.GoBot.say('Duration: {}  | :thumbsup:: {} | :thumbsup:: {}'.format(player.duration, player.likes, player.dislikes)) 
        

    @commands.command(pass_context=True)
    async def queue(self, ctx, url):
        server = ctx.message.server
        voice_client = self.GoBot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: self.check_queue(server.id))

        if server.id in YT.queues:
            YT.queues[server.id].append(player)
        else:
            YT.queues[server.id] = [player]
        await self.GoBot.say('Queued: {}'.format(player.title))

def setup(GoBot):
    GoBot.add_cog(YT(GoBot))