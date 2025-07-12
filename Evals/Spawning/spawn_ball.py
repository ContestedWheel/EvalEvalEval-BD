COUNTRYBALL = "countryball"

from ballsdex.settings import settings
from ballsdex.packages.countryballs.countryball import BallSpawnView
from ballsdex.core.models import Ball

algo = "evalspawn"
channel = ctx.channel
ball = BallSpawnView(bot, await Ball.get(country=COUNTRYBALL))
ball.algo = algo
await ball.spawn(channel)