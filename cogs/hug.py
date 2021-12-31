import discord, random
from discord.ext import commands

class hug(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        if user:
            randomgifs = [
            "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif",
            "https://c.tenor.com/zirc8LTWVUkAAAAC/hug-anime.gif",
            "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif",
            "https://c.tenor.com/OIKUxVk2Sm8AAAAC/hug.gif"
            ]

            embed = discord.Embed(title = "Przytulas", description = f"{user.mention} zostałeś/aś przytulony/a przez {ctx.author.mention}", color = user.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            embed.set_image(url = random.choice(randomgifs))

            msg = await ctx.send(embed = embed)
            await msg.add_reaction("😺")
            await msg.add_reaction("😽")
            await msg.add_reaction("😻")
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.hug <@wzmianka>**", color = 0xe74c3c))
            await msg.add_reaction("❌")
            
def setup(client):
    client.add_cog(hug(client))