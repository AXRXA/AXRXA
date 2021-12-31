import discord, random
from discord.ext import commands

class kiss(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None):
        if user:
            randomgifs = [
            "https://c.tenor.com/03wlqWILqpEAAAAC/highschool-dxd-asia.gif",
            "https://c.tenor.com/TnjL6WcdkkwAAAAM/anime-kiss.gif",
            "https://c.tenor.com/F02Ep3b2jJgAAAAC/cute-kawai.gif",
            "https://c.tenor.com/CtpjMGItICQAAAAC/anime-kissing.gif"
            ]

            embed = discord.Embed(title = "Buziaczek", description = f"{user.mention} dostałeś/aś buziaka od {ctx.author.mention}", color = user.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            embed.set_image(url = random.choice(randomgifs))

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("😺")
            await msg.add_reaction("😽")
            await msg.add_reaction("😻")
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.kiss <@wzmianka>**", color = 0xe74c3c))
            await msg.add_reaction("❌")
            
def setup(client):
    client.add_cog(kiss(client))