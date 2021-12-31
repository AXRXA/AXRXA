import discord
from discord.ext import commands

class serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["server"])
    async def serverinfo(self, ctx, user : discord.Member = None):
            if user == None:
                user = ctx.author
            roles = [role for role in ctx.guild.roles]

            embed = discord.Embed(title = f"Informacje o serwerze **{ctx.guild.name}**", color = ctx.author.color)
            embed.set_thumbnail(url = ctx.guild.icon_url),
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        
            embed.add_field(name = "ID:", value = f"🆔 {ctx.guild.id}", inline = False)
            embed.add_field(name = "Właściciel:", value = f"👑 {ctx.guild.owner}")
            embed.add_field(name = "Liczba osób:", value = f"📌 {len(ctx.guild.members)}", inline = False)
            embed.add_field(name = 'Serwer stworzony:', value = f"🗓 {ctx.guild.created_at.strftime('%d/%m/%Y, %H:%M')}", inline = False)
            embed.add_field(name = f"Role:", value = len(ctx.guild.roles), inline = False)
            embed.add_field(name = f"Najwyższa rola:", value = ctx.guild.roles[-1], inline = False)

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(serverinfo(client))