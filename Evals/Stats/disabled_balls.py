from ballsdex.core.models import Ball

balls = await Ball.all()
disabledballs = [ball for ball in balls if not ball.enabled]
if disabledballs:
    for ball in disabledballs:
        print(ball)
else:
    print("There are no disabled balls")
