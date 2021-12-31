import discord, asyncio, re
from discord.ext import commands

class tempmute(commands.Cog):

    def __init__(self, client):
        self.client = client

    class TimeConverter(commands.Converter):
        async def convert(self, ctx, argument):
            time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
            time_dict = {"h":3600, "s":1, "m":60, "d":86400}

            args = argument.lower()
            matches = re.findall(time_regex, args)
            time = 0
            for v, k in matches:
                try:
                    time += time_dict[k]*float(v)
                except KeyError:
                    raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
                except ValueError:
                    raise commands.BadArgument("{} is not a number!".format(v))
            return time

    
    @commands.command()
    async def tempmute(self, ctx, user: discord.Member = None, duration: TimeConverter = None, *, reason = None):
        if user and duration and reason:
            mutedrole = discord.utils.get(ctx.message.guild.roles, name = "Wyciszony")
            await user.add_roles(mutedrole)

            embed = discord.Embed(title = "Wyciszenie", description = f"Użytkownik {user.mention} został wyciszony przez {ctx.author.mention} za **{reason}** na czas **{duration:.0f}s.**", color = 0x992d22)
            embed.set_thumbnail(url = user.avatar_url)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

            await asyncio.sleep(duration)
            await user.remove_roles(mutedrole)
            embed1 = discord.Embed(title ="Odciszenie", description = f"Użytkownik {user.mention} został odciszony.", color = 0x992d22)
            embed1.set_thumbnail(url = user.avatar_url)
            embed1.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed1) 
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.tempmute <@wzmianka> <czas> <powód>**", color = 0xe74c3c))
            await msg.add_reaction("❌")

def setup(client):
    client.add_cog(tempmute(client))