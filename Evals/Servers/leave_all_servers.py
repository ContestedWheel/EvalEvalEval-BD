await asyncio.gather(*[guild.leave() for guild in bot.guilds])
