b.eval ball = await Ball.get(country="COUNTRY NAME HERE.")
ball.short_name = "SHORT NAME HERE"
await ball.save()