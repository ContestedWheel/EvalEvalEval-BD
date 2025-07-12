ball = await Ball.get(country="country name here")
emoji = bot.get_emoji(int(ball.emoji_id))
await ctx.send(emoji)