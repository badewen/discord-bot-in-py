import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
      self.client = client


    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
      embed=discord.Embed(title='Command lists',   
                           description='List of commands',
                            color=0xfff700)

      embed.add_field(name='Moderation',
                    value="`.help moderation`(**DISCONTINUED**)",
                    inline=False)

      embed.add_field(name='Entertainment',
                    value='`.help entertainment`',
                    inline=False)

      embed.add_field(name="Others", 
                      value="`.help others`", 
                      inline=False)

      await ctx.send(embed=embed)

    @help.command()
    async def moderation(self, ctx):

      embed=discord.Embed(title="Moderation commands (**DISCONTINUED**)", 
      description="discontinued cause im lazi :D", color=0xfff700)

      embed.add_field(name="Commands that still working", value="`purge`", inline=False)

      embed.add_field(name="Not working anymore", value="`ban`, `unban`, `kick`", inline=False)

      embed.set_footer(text="imagine moderation lol")

      await ctx.send(embed=embed)

    @help.command()
    async def entertainment(self, ctx):

      embed=discord.Embed(title="Entertainment commands", 
      description="just entertainment/fun command. what u expect lmao", color=0xfff700)

      embed.add_field(name="List of commands", value="`say`, `8ball`,", inline=False)

      embed.set_footer(text="L")

      await ctx.send(embed=embed)

    @help.command()
    async def others(self, ctx):

      embed=discord.Embed(title="Other commands", 
      description="idek just for uncategorized commands(?) ig who knows", color=0xfff700)

      embed.add_field(name="List of commands", value="``, `ping`", inline=False)

      embed.set_footer(text="suggest duh")

      await ctx.send(embed=embed)

    @help.command()
    async def say(self, ctx):

      embed=discord.Embed(title='how to use say command', color=0xfff700)

      embed.add_field(name='say command', value='`usage : say (ur word here) but if u going to make the bot say more than 1 word then say "(ur word here)"`')
      
      await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Help(client))