COUNTRYBALL = "countryball"
HP_BUFF = 1000
ATK_BUFF = 1000
SPECIAL = None

from ballsdex.settings import settings
from ballsdex.packages.countryballs.countryball import BallSpawnView
from ballsdex.core.models import Ball, Special

algo = "evalspawn"
channel = ctx.channel
ballinstance = await Ball.get(country=COUNTRYBALL)

ball = BallSpawnView(bot, ballinstance)
ball.hp_bonus = HP_BUFF
ball.atk_bonus = ATK_BUFF
ball.special = await Special.get(name=SPECIAL) if SPECIAL else None

ball.algo = algo
await ball.spawn(channel)