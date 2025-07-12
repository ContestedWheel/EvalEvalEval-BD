oldPlayer = await Player.get(discord_id=)
newPlayer = await Player.get(discord_id=)

balls = await BallInstance.filter(player=oldPlayer)
for ball in balls:
    ball.player = newPlayer
    await ball.save()