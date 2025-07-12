server = discord.utils.get(bot.guilds, id=server_id_here)

if server:
    await server.leave()
else:
    await ctx.send("this server doesnt exist")
