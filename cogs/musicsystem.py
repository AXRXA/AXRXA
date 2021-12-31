import discord
from discord.ext import commands
import youtube_dl
from discord.utils import get
class musicsystem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = f"Hmm.. Nie mogę cię zlokalizować na żadnym kanale głosowym. Upewnij się, że jesteś połączony.", color=0xe67e22))
            await msg.add_reaction("❌")

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = f"Nie jestem połączony na żadnym kanale głosowym.", color=0xe67e22))
            await msg.add_reaction("❌")

    @commands.command(pass_context = True, aliases=['p'])
    async def play(self, ctx, *, url = None):
        if not url:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = f"Poprawne użycie: .play <url>", color=0xe67e22))
            await msg.add_reaction("❌")
        elif not (ctx.author.voice):
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = f"Hmm.. Nie mogę cię zlokalizować na żadnym kanale głosowym. Upewnij się, że jesteś połączony.", color=0xe67e22))
            await msg.add_reaction("❌")
        else:
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format':"bestaudio"}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download = False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)

    @commands.command(pass_context = True, aliases=['stop'])
    async def pause(self, ctx):
        server = ctx.message.guild
        voice = server.voice_client  
        if voice and voice.is_playing():
            voice.pause()
            msg = await ctx.send(embed = discord.Embed(description = f"Utwór został zatrzymany przez {ctx.author.mention}", color = ctx.author.color))
            await msg.add_reaction("✅")
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = f"Utwór nie został zatrzymany. Prawdopodobnie żaden utwór nie jest odtwarzany lub został już zatrzymany wcześniej.", color=0xe67e22))
            await msg.add_reaction("❌")

    @commands.command(pass_context = True)
    async def resume(self, ctx):
        server = ctx.message.guild
        voice = server.voice_client  
        if voice and voice.is_paused():
            voice.resume()
            msg = await ctx.send(embed = discord.Embed(description = f"Utwór został wznowiony przez {ctx.author.mention}", color = ctx.author.color))
            await msg.add_reaction("✅")
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = f"Utwór nie został wznowiony. Prawdopodobnie żaden utwór nie jest odtwarzany lub został już wznowiony wcześniej.", color=0xe67e22))
            await msg.add_reaction("❌")

    @commands.command(pass_context = True, aliases = ['s'])
    async def skip(self, ctx):
        server = ctx.message.guild
        voice = server.voice_client  
        if voice and voice.is_playing():
            voice.skip()
        else:
            await ctx.send("test")

def setup(client):
    client.add_cog(musicsystem(client))