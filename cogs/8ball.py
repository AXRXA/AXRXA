import discord
from discord.ext import commands
import random

class eightball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question = None):
        if question:
            answers = ['Tak.', 'Nie.', 'Być może.', 'Spytaj mnie później.', 'Nie odpowiem na to pytanie.', 'Nie mam teraz czasu.', 'Oczywiście.', 'XDD.', 'No nie wiem.', 'Aż tak głupi nie jestem.', 'Zastanowie się.', 'Daj mi chwilę.', 'Aha.', 'ok.', 'Domyśl się.']

            embed = discord.Embed(title = "8ball", color = ctx.author.color)
            embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

            embed.add_field(name = ":8ball: Pytanie:", value = question, inline = False)
            embed.add_field(name = ":8ball: Odpowiedź:", value = random.choice(answers), inline = False)

            msg = await ctx.send(embed=embed)
            await msg.add_reaction("😂")
            await msg.add_reaction("😐")
            await msg.add_reaction("😢")
        else:
            msg = await ctx.send(embed = discord.Embed(title = "ERROR", description = "Poprawne użycie: **.8ball <pytanie>**", color = 0xe74c3c))
            await msg.add_reaction("❌")


def setup(client):
    client.add_cog(eightball(client))