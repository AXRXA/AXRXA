import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        
        embed = discord.Embed(title = "Pomoc", description = "Xi to nowy rozwijający się bot, który na obecną chwilę nie ma za dużo komend. Naszym celem jest wyróżnienie się spośród innych botów.", color = ctx.author.color)
        embed.set_thumbnail(url = ctx.bot.user.avatar_url)
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

        embed.add_field(name = "🔹 • Ogólne:", value = "`.userinfo`, `.serverinfo`, `.botinfo`, `.invite`, `.ping`", inline = False)
        embed.add_field(name = "🔸 • Moderacja:", value = "`.clear`, `.ban`, `.kick`, `.tempmute`, `.warn`, `.warns`, `.unwarn`", inline = False)
        embed.add_field(name = "🔹 • 4fun:", value = "`.8ball`, `.avatar`, `.hug`, `.kiss`, `.slap`, `.cry`, `.happy`, `.lgbt`, `.iq`, `.rep`, `.replist`, `.repleaderboard`, `.animal`", inline = False)
        embed.add_field(name = "🔸 • Muzyka:", value = "`.join`, `.leave`, `.play`, `.pause`, `.resume`", inline = False)
        embed.add_field(name = "🔹 • Ekonomia:", value = "`.work`, `.balance`, `.deposit`, `.withdraw`, `.give`, `.rob`, `.leaderboard`, `.fortunewheel`", inline = False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(help(client))