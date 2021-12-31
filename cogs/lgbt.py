import discord, random
from discord.ext import commands

class lgbt(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lgbt(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

            embed = discord.Embed(title = "LGBT", description = f"Jesteś w **{random.randrange(101)}%** lgbt.", color = ctx.author.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("😹")
            await msg.add_reaction("😺")
            await msg.add_reaction("😻")
        else:
            embed = discord.Embed(title = "ILORAZ INTELIGENCJI", description = f"Użytkownik {user.mention} jest w **{random.randrange(101)}%** lgbt.", color = user.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("😹")
            await msg.add_reaction("😺")
            await msg.add_reaction("😻")

def setup(client):
    client.add_cog(lgbt(client))