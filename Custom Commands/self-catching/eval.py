# This is an eval example to spawn a self catching ball, make sure you added the injection code first!


from ballsdex.packages.countryballs.countryball import BallSpawnView
ball = BallSpawnView(bot, await Ball.get(country="BALL_NAME"))
ball.catch_by_itself = INT_SECONDS
await ball.spawn(bot.get_channel(CHANNEL_ID))
