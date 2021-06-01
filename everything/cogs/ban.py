import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      if member.top_role >= ctx.author.top_role:
        await ctx.send('you can only ban people below you')
        return
      await member.ban(reason=reason)
      await ctx.send(f'user banned ')
      
def setup(client):
  client.add_cog(ban(client))