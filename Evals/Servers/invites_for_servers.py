invites = []
for guild in bot.guilds:
    if guild.member_count <15:
        for c in guild.text_channels:
            # make sure the bot can actually create an invite
            if c.permissions_for(guild.me).create_instant_invite:

                    invite = await c.create_invite()
                    invites.append(invite)
                    await ctx.send(invite)

                    break
