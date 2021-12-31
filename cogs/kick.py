import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user : discord.Member = None, *, reason = None):
        if user and reason:
            await user.kick(reason = reason)
            embed = discord.Embed(title = "Wyrzucenie", description = f"Użytkownik {user.mention} został wyrzucony przez {ctx.author.mention} za **{reason}**.", color = 0x992d22)
            embed.set_thumbnail(url = user.avatar_url)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.kick <@wzmianka> <powód>**", color = 0xe74c3c))
            await msg.add_reaction("❌")

    @kick.error
    async def kick_error(error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Brak permisji!"
            await ctx.send(ctx.message.channel, text)

    
def setup(client):
    client.add_cog(clear(client))