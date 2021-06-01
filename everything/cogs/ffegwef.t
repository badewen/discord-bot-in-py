@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=6):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'**{amount}** Messages has been deleted')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'user banned ')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'user banned ')


@client.command()
@commands.has_permissons(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unabn(user)
        await ctx.send(f'Unbanned {user.mention}')
        return





        @ban.error
    async def ban_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send('You dont have the permission to do that.')    
      if isinstance(error, commands.CommandInvokeError):
        await ctx.send('I could not ban that member.')