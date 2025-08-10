
import random
from ballsdex.core.models import Ball, Player, Special, BallInstance
from ballsdex.settings import settings

ball = await Ball.get(country="INSERT_COUNTRY")
player = await Player.get(discord_id=INSERT_DISCORD_ID)
special = await Special.get(name="INSERT_SPECIAL") # Set to "None" if you don't want a Special.
shiny = INSERT_True_OR_False
atk = random.randint(-20, 20)
hp = random.randint(-20, 20)
amount = INSERT_NUMBER

for i in range(1):
    await BallInstance.create(ball=ball, player=player, shiny=shiny, attack_bonus=atk, health_bonus=hp, special=special)

await ctx.send(f"Successfully given <@{player.discord_id}> {ball} {amount} times!")
