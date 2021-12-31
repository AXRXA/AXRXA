import discord
from discord.ext import commands

class avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, user : discord.Member = None):
            if user == None:
                user = ctx.author

            embed = discord.Embed(title = "Avatar", color = ctx.author.color)
            embed.set_image(url = user.avatar_url)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(avatar(client))