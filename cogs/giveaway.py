import discord
from discord.ext import commands
import asyncio, random

class giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["giveaway", "giveawaycreate", "addgiveaway", "gadd", "addg", "giveawayadd"])
    async def gcreate(ctx, time = None, *, prize = None):
        if time or prize == None:
            await ctx.send("Poprawne użycie: .gcreate <czas> <nagroda>")
        else:
            embed = discord.Embed(title = "GIVEAWAY!", description = f"{ctx.author.mention} rozdaje **{prize}**. Aby wziąć udział, zareaguj emoji poniżej:")
            time_convert = {"s":1, "m":60, "h":3600, "d":86400}
            gtime = int(time[0]) * time_convert[time[-1]]
            embed.set_footer(text = f"Giveaway zakończy się za {time}")
            gmsg = await ctx.send(embed = embed)

            await gmsg.add_reaction("🎉")
            await asyncio.sleep(gtime)

            new_gmsg = await ctx.channel.fetch_message(gmsg.id)

            users = await gmsg.reactions[0].users().flatten()
            users.pop(users.index(ctx.client.user))

            winner = random.choice(users)

            await ctx.send(f"Użytkownik {winner.mention} wygrywa **{prize}**. Serdeczne gratulacje od Xi!")


def setup(client):
    client.add_cog(giveaway(client))