from discord.ext import commands

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, arg):
      await ctx.send(arg)

    @say.error
    async def say_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('provide the required arguments')

def setup(client):
    client.add_cog(Say(client))
