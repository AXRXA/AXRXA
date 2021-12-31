import discord, random
from discord.ext import commands
from PIL import Image
from io import BytesIO


class rip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rip(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        rip = Image.open("grave.jpg")
        asset = user.avatar_url_as(size = 512)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((118, 113))
        rip.paste(profilepic, (104, 153))
        rip.save("prip.jpg")

        await ctx.send(file = discord.File("sgrave.jpg"))


def setup(client):
    client.add_cog(rip(client))