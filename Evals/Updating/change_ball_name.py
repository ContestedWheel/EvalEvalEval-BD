ball = await Ball.get(country="OLD NAME.")
ball.country = "NEW NAME."
await ball.save()