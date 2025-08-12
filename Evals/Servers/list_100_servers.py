# The number can be lowered by replacing the 100 in "sorted_guilds[:100]"
# For example, if I wanted to list 50 servers instead, I would replace it with "sorted_guilds[:50]"
# Make sure to keep the colon when replacing the number, or the eval will not work.

sorted_guilds = sorted(bot.guilds, key=lambda guild: guild.member_count, reverse=True)
top_10_guilds = sorted_guilds[:100]

for guild in top_10_guilds:

    await ctx.send(f"{guild.name} - Member Count: {guild.member_count} - ID:{guild.id}")

