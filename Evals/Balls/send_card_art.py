ball = await Ball.get(country="name here")
file_location = "." + ball.collection_card
await ctx.send(file=discord.File(file_location))