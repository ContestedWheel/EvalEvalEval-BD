ball = await Ball.get(country="name here")
file_location = "./admin_panel/media/" + ball.wild_card
await ctx.send(file=discord.File(file_location))
