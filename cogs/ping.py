import discord
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = "Ping", description = "Wyświetla ping bota.", color = ctx.author.color)
        embed.add_field(name = "Ping bota:", value = f"{round(ctx.bot.latency * 1000)}ms")
        embed.set_thumbnail(url = ctx.author.avatar_url)
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(test(client))