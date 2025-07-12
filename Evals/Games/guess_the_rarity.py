import random, asyncio
from ballsdex.core.models import Ball
balls = await Ball.filter(enabled=True)
ball = random.choice(balls)
file_location = "." + ball.spawnPicture
await ctx.send("Guess the rarity of this ball!")
await ctx.send(file=discord.File(file_location))
await asyncio.sleep(4)
await ctx.send("The rarity of the ball was...")
await asyncio.sleep(1)
await ctx.send(ball.rarity)