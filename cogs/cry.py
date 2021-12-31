import discord, random
from discord.ext import commands

class cry(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cry(self, ctx):
            randomgifs = [
            "https://c.tenor.com/bMSZQ4j3CQkAAAAC/anime-cry.gif",
            "https://c.tenor.com/ZK3DOFspBAUAAAAC/akko-qq.gif",
            "https://c.tenor.com/O6mJ5XEY5tQAAAAC/cry-pleure.gif",
            "https://c.tenor.com/VGvz6lNaXkIAAAAC/satania-cry-satania.gif"
            ]

            embed = discord.Embed(title = "Smuteczek", description = f"{ctx.author.mention} jest ogromnie smutny/a :(", color = ctx.author.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            embed.set_image(url = random.choice(randomgifs))

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("🙀")
            await msg.add_reaction("😽")
            await msg.add_reaction("😿")


def setup(client):
    client.add_cog(cry(client))