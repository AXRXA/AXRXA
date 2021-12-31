import discord, random
from discord.ext import commands

class happy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def happy(self, ctx):
            randomgifs = [
            "https://c.tenor.com/FaW4VactWBsAAAAC/anime-blush.gif",
            "https://c.tenor.com/cixwWtz9bn8AAAAC/happy-happy-anime.gif",
            "https://c.tenor.com/zy4PbIW2Ig0AAAAC/ouran-ouran-high-school-host-club.gif",
            "https://c.tenor.com/NPwbaSvkD9cAAAAC/anime-yui.gif"
            ]

            embed = discord.Embed(title = "Uśmieszek", description = f"{ctx.author.mention} jest szczęśliwy/a :D", color = ctx.author.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            embed.set_image(url = random.choice(randomgifs))

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("🙀")
            await msg.add_reaction("😽")
            await msg.add_reaction("😿")


def setup(client):
    client.add_cog(happy(client))