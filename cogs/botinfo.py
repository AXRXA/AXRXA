import discord
from discord.ext import commands

class botinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions()
    async def botinfo(self, ctx):
        developer_id = "829796244770914332"
        tester_id = "512694302036721667"

        embed = discord.Embed(title = "Autorzy", description = "Twórcy i testerzy bota Xi.", color = ctx.author.color)

        embed.set_thumbnail(url = ctx.guild.icon_url),
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

        embed.add_field(name = "Developer:", value = f"<@{developer_id}>", inline = False)
        embed.add_field(name = "Tester:", value = f"<@{tester_id}>", inline = False)
        embed.add_field(name = "Wersja:", value = "1.0")

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(botinfo(client))