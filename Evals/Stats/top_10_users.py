from tortoise.functions import Count

players = await Player.annotate(balls_count=Count("balls")).order_by("-balls_count").limit(10)
for player in players:
  print(f"{player.balls_count}: {await bot.fetch_user(int(player.discord_id))}")
