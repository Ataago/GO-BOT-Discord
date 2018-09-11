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
            #yield self.GoBot.say('playing in queue')
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
        secs =  (player.duration)%60
        mins = int(((player.duration)/60)%60)
        hrs =  int((player.duration)/3600)
        embed = discord.Embed(
                color = discord.Color.red(), 
                title = "Playing " + player.title ,
                description = 'by **' + player.uploader + "**       Duration: "+ str(hrs) + ':' + str(mins) + ':' + str(secs) + "\n\n Requested by: **" + ctx.message.author.name + "**"
        )
        #embed.add_field(name = 'Duration: ', value = int((player.duration)/3600) + int(((player.duration)/60)%60) + (player.duration)%60, inline=True)
       # embed.add_field(name = ':thumbsup:', value = player.like , inline=True)
        #embed.add_field(name = ':thumbsdown:', value = player.dislike , inline=True)
       # embed.set_footer(text = 'as requested by **' + ctx.message.author.name + '**')
        await self.GoBot.say(embed = embed)
        #await self.GoBot.say('Playing **{}** by **{}**'.format(player.title, player.uploader))
        #await self.GoBot.say('Duration: **{}**:**{}**:**{}**  | :thumbsup:: **{}** | :thumbsdown:: **{}**'.format(int((player.duration)/3600), int(((player.duration)/60)%60), (player.duration)%60, player.likes, player.dislikes)) 
        #await self.GoBot.say('as requested by **{}**'.format(ctx.message.author.name))
        

    @commands.command(pass_context=True)
    async def queue(self, ctx, url = 'check'):
        if url == 'check':
            await self.GoBot.say("Current Queue is:")
            await self.GoBot.say(self.queues)
            return
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