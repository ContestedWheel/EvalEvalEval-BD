ball = await Ball.get(country="COUNTRY NAME")
ball.catch_names = ball.catch_names + ";NEW CATCH NAME"
await ball.save()

# The semicolon is not a typo, it's there to make the catch name valid (example: catchname1;catchname2). Otherwise, it will look like this in the panel and not work:
# catchname1catchname2
