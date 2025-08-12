from ballsdex.core.models import Ball
balls = await Ball.all()

total = sum(ball.rarity for ball in balls if ball.enabled)

chances = {ball: round((ball.rarity / total)*100000)/1000 for ball in balls if ball.enabled}
chances = dict(sorted(chances.items(), key=lambda item: item[1]))

resp = ""
for ball, chance in chances.items():
  resp += f"{ball.country} has a {chance}% change of spawning\n"
return resp
