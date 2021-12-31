import discord
from discord.ext import commands

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions()
    async def invite(self, ctx):
        embed = discord.Embed(title = "Zaproszenie", description = "Zaproś Xi na swój serwer oraz dołącz do serwera.", color = ctx.author.color)

        embed.set_thumbnail(url = ctx.guild.icon_url),
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

        embed.add_field(name = "Bot:", value = "[kliknij!](https://discord.com/api/oauth2/authorize?client_id=909506677429121064&permissions=8&scope=bot)", inline = False)
        embed.add_field(name = "Serwer:", value = "[kliknij!](https://discord.gg/BDG7CEyDMK)")

        await ctx.send(embed = embed)
def setup(client):
    client.add_cog(clear(client))