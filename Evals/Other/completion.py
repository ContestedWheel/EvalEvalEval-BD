import random
balls = await Ball.filter(enabled=True)
player = await Player.get(discord_id=User ID here)
for ball in balls:
    await BallInstance.create(ball=ball, player=player, attack_bonus=random.randint(+0,0), health_bonus=random.randint(+0,0), shiny=False)