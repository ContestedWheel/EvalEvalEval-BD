ball = await Ball.get(country="COUNTRY NAME HERE")
ball.enabled = True/False
await ball.save()