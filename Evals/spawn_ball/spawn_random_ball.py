from ballsdex.packages.countryballs.countryball import BallSpawnView
from ballsdex.settings import settings

algo = "evalspawn"
channel = ctx.channel
ball = await BallSpawnView.get_random(bot)
ball.algo = algo
await ball.spawn(channel)
