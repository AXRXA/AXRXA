import discord, random
from discord.ext import commands

class iq(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def iq(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

            embed = discord.Embed(title = "Iloraz inteligencji", description = f"Posiadasz drogi użytkowniku **{random.randrange(303)}** iq.", color = ctx.author.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("😹")
            await msg.add_reaction("😺")
            await msg.add_reaction("😻")
        else:
            embed = discord.Embed(title = "Iloraz inteligencji", description = f"Użytkownik {user.mention} posiada **{random.randrange(303)}** iq.", color = user.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("😹")
            await msg.add_reaction("😺")
            await msg.add_reaction("😻")
            
def setup(client):
    client.add_cog(iq(client))