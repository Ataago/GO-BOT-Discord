# @author Ataago 
# @license GPL-3.0

import discord
from discord.ext import commands

class YT():
    def __init__(self, GoBot):
        self.GoBot = GoBot
    
    players = {}
    queues = {}

    @commands.command(pass_context = True)
    async def next(self, ctx):
        serverID = ctx.message.server.id
        YT.players[serverID].stop()
        #voice_client = self.GoBot.voice_client_in(server)
        #player = await voice_client.create_ytdl_player(url, after=lambda: self.check_queue(server.id))

        if YT.queues[id] != []:
            player = YT.queues[id].pop()
            YT.players[id] = player
            player.start()


    def check_queue(self, id):
        if YT.queues[id] != []:
            player = YT.queues[id].pop(0)
            YT.players[id] = player
            player.start()
            print('this is from queue',player.title)
            #await self.GoBot.say('playing in queue')
            #self.GoBot.send_message('Playing {}'.format(player.title))
            #await self.GoBot.say('Duration: {}  | :thumbsup:: {} | :thumbsup:: {}'.format(player.duration, player.likes, player.dislikes)) 

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
        await self.GoBot.delete_message(ctx.message)
        await self.GoBot.say('Playing **{}** by **{}**'.format(player.title, player.uploader))
        await self.GoBot.say('Duration: **{}**:**{}**:**{}**  | :thumbsup:: **{}** | :thumbsdown:: **{}**'.format(int((player.duration)/3600), int(((player.duration)/60)%60), (player.duration)%60, player.likes, player.dislikes)) 
        await self.GoBot.say('as requested by **{}**'.format(ctx.message.author.name))
        

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

    @commands.command(pass_context = True)
    async def vol(self, ctx):
        serverID = ctx.message.server.id
        YT.players[serverID].volume(2)
        print('next line')


    @commands.command(pass_context=True)
    async def pause(self, ctx):
        serverID = ctx.message.server.id
        YT.players[serverID].pause()

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        serverID = ctx.message.server.id
        YT.players[serverID].stop()
        YT.queues = {}

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        serverID = ctx.message.server.id
        YT.players[serverID].resume()
  
def setup(GoBot):
    GoBot.add_cog(YT(GoBot))