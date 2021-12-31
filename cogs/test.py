import discord, random
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def xd(self, ctx):
        XD = ['XD', 'XDDDD', 'Xd', 'Xddddd', 'xd', 'xdddddddddd', 'xD', 'xDDDDDDD', 'XDdDDDDDDDdDDddddDDD', 'XDDDDDDDDDDDDDDDD', 'xddddddddddddddddd', 'xDDDDDDDDDDD', 'Xdddddddddddddd', 'xDDdddDDDD', 'Xddddddddddd.']
        await ctx.send(embed = discord.Embed(description = random.choice(XD), color = ctx.author.color))


def setup(client):
    client.add_cog(test(client))