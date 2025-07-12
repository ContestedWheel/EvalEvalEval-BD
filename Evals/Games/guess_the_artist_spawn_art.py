import random, asyncio
from ballsdex.core.models import Ball
balls = await Ball.filter(enabled=True)
ball = random.choice(balls)
file_location = "." + ball.wild_card
await ctx.send("Guess the artist(s) of this spawn art!")
await ctx.send(file=discord.File(file_location))
await asyncio.sleep(4)
await ctx.send("The artist(s) of the spawn art was....")
await asyncio.sleep(1)
await ctx.send(ball.credits)