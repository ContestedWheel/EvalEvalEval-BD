from ballsdex.core.models import Regime

ball = await Ball.get(country="INSERT_COUNTRY")
ball.regime = await Regime.get(name="INSERT_NEW_REGIME")
await ball.save()
