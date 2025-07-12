ball = await Ball.get(country="COUNTRY NAME")
ball.credits = CREDITS
await ball.save()