import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(manage_messages = True)
    async def clear(self, ctx, amount: int = None):
        if amount:
            await ctx.channel.purge(limit = amount + 1)

            embed = discord.Embed(description = f"Chat został wyczyszczony o **{amount}** wiersz(y/e) przez użytkownika {ctx.author.mention}", color = 0x9b59b6)
            await ctx.channel.send(embed =  embed, delete_after=True)
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.clear <ilość>**", color = 0xe74c3c))
            await msg.add_reaction("❌")

    @clear.error
    async def clearerror(ctx, error):
        if isinstance(error, MissingPermissions):
            text = "Brak permisji!"
            await ctx.send(ctx.message.channel, text)
    

def setup(client):
    client.add_cog(clear(client))