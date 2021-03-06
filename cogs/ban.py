import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user : discord.Member = None, *, reason = None):
        if user and reason:
            await user.ban(reason = reason)
            embed = discord.Embed(title = "Banicja", description = f"Użytkownik {user.mention} został zbanowany przez {ctx.author.mention} za **{reason}**.", color = 0x992d22)
            embed.set_thumbnail(url = user.avatar_url)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.ban <@wzmianka> <powód>**", color = 0xe74c3c))
            await msg.add_reaction("❌")



    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, user = None):
        if user:
            banned = await ctx.guild.bans()
            member_name, member_discriminator = user.split('#')

            for ban_entry in banned:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed = discord.Embed(title = "Unbanicja", description = f"Użytkownik **{user.mention}** został odbanowany przez {ctx.author.mention}", color = 0x992d22)
                    embed.set_thumbnail(url = user.avatar_url)
                    embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed = embed)
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.unban <nazwa#id>**", color = 0xe74c3c))
            await msg.add_reaction("❌")


    @ban.error
    async def ban_error(error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Brak permisji!"
            await ctx.send(ctx.message.channel, text)
    
    
    @unban.error
    async def unban_error(error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Brak permisji!"
            await ctx.send(ctx.message.channel, text)

    
def setup(client):
    client.add_cog(clear(client))