import discord, random
from discord.ext import commands

class slap(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):
        if user:
            randomgifs = [
            "https://c.tenor.com/pHCT4ynbGIUAAAAC/anime-girl.gif",
            "https://c.tenor.com/idgTDL_WC6EAAAAC/loli-cute.gif",
            "https://c.tenor.com/HTHoXnBc400AAAAd/in-your-face-slap.gif",
            "https://c.tenor.com/ra17G61QRQQAAAAC/tapa-slap.gif"
            ]

            embed = discord.Embed(title = "Listwa", description = f"{user.mention} dostałeś/aś listwę od {ctx.author.mention}", color = user.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            embed.set_image(url = random.choice(randomgifs))

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("🙀")
            await msg.add_reaction("😾")
            await msg.add_reaction("😿")
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Użyj: **.slap <@wzmianka>**", color = 0xe74c3c))
            await msg.add_reaction("❌")
def setup(client):
    client.add_cog(slap(client))