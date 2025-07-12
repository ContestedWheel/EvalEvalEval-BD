b.eval ball = await Ball.get(country="COUNTRY NAME HERE.")
ball.short_name = "SHORT NAME HERE"
await ball.save()

# The short name is the text that appears on top of the card that is next to the economy icon.
