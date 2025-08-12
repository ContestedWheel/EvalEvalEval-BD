sorted_guilds = sorted(bot.guilds, key=lambda guild: guild.member_count, reverse=True)
top_10_guilds = sorted_guilds[:100]

for guild in top_10_guilds:

    await ctx.send(f"{guild.name} - Member Count: {guild.member_count} - ID:{guild.id}")
