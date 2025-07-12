ball = await Ball.get(country="COUNTRY NAME")
ball.health = HEALTH
await ball.save()