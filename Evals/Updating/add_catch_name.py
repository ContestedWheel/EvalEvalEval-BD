ball = await Ball.get(country="COUNTRY NAME")
ball.catch_names = ball.catch_names + ";NEW CATCH NAME"
await ball.save()