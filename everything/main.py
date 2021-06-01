import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from webserver import keep_alive

client = commands.Bot(command_prefix='.',  case_insensitive=True)
status = cycle(['meinkraf', 'sleep'])
my_secret = os.environ['DISCORD_BOT_TOKEN']
lol = discord.AutoShardedClient()
lmao = client.connect()
client.remove_command('help')

def is_it_me(ctx):
    return ctx.author.id == 741846750867750972


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    change_status.start()
    print('bot is ready')

@tasks.loop(seconds=12)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
client.run(my_secret)
