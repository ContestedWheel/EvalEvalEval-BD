# Replace `0` with the user's ID.
USER_ID = 0


import random

from ballsdex.settings import settings

player = await Player.get(discord_id=USER_ID)

await ctx.send("Giving full completion...\n-# This may take a while.")

async for ball in Ball.filter(enabled=True):
    await BallInstance.create(
        ball=ball,
        player=player,
        attack_bonus=random.randint(-settings.max_attack_bonus, settings.max_attack_bonus),
        health_bonus=random.randint(-settings.max_health_bonus, settings.max_health_bonus)
    )

await ctx.send("Finished giving full completion!")
