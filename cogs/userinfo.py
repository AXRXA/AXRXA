import discord
from discord.ext import commands

class userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["user", "info"])
    async def userinfo(self, ctx, user : discord.Member = None):
            if user == None:
                user = ctx.author
            roles = [role for role in user.roles]

            embed = discord.Embed(title = f"Informacje użytkowniku **{user}**", color = ctx.author.color)
            embed.set_thumbnail(url = user.avatar_url),
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        
            embed.add_field(name = "ID:", value = f"🆔 {user.id}", inline = False)
            embed.add_field(name = "Nazwa:", value = f"📌 {user.display_name}", inline = False)
            embed.add_field(name = 'Konto stworzone:', value = f"🗓 {user.created_at.strftime('%d/%m/%Y, %H:%M')}", inline = False)
            embed.add_field(name = 'Dołączył:', value = f"🗓 {user.joined_at.strftime('%d/%m/%Y, %H:%M')}", inline = False)

            embed.add_field(name = f"Role: ({len(roles)})", value = " ".join([role.mention for role in roles]), inline = False)
            embed.add_field(name = f"Najwyższa rola:", value = user.top_role.mention, inline = False)

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(userinfo(client))