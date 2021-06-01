import discord
from discord.ext import commands
from discord.utils import get


class Help_moderation(commands.Cog):

    def __init__(self, client):
      self.client = client

  

    @help.command()
    async def moderation(self, ctx):
      embed=discord.Embed(title="Moderation commands (**DISCONTINUED**)", 
      description="discontinued cause im lazi :D", color=0xfff700)

      embed.add_field(name="Commands that still working", value="`purge`, `mute`", inline=False)

      embed.add_field(name="Not working anymore", value="`ban`, `unban`, `kick`", inline=False)

      embed.set_footer(text="imagine moderation lol")

      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help_moderation(client))