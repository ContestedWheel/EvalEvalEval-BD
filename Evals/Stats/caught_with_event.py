special = await Special.get(name="special name here")
balls = await BallInstance.filter(special=special).prefetch_related("ball")
for b in balls:
        print(b.ball)
