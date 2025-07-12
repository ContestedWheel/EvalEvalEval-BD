balls = await Ball.all()
balls = [ball for ball in balls if ball.enabled]
balls.sort(key=lambda ball: ball.rarity)
for ball in balls:
 print(f"{ball.rarity} - {ball}") 