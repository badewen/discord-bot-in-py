from discord.ext import commands

class Purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount=6):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'**{amount}** Messages has been     deleted')
        

    @purge.error
    async def purge_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send('you dont have the permission to do that.')

def setup(client):
    client.add_cog(Purge(client))
    