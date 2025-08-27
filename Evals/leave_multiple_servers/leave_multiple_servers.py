await asyncio.gather(*[guild.leave() for guild in bot.guilds[:50]])
# A limit of 50 servers has been added to this eval due to rate limting issues.
