ball = await Ball.get(country="COUNTRY NAME HERE")
ball.enabled = True/False
await ball.save()

# If true:
# Ball will show up in completion and spawn if rarity is not 0.

# If false:
# Ball will not show up in completion.
