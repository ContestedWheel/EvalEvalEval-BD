ball = await Ball.get(country="COUNTRY NAME HERE")
ball.tradeable = True/False
await ball.save()