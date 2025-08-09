from tortoise.functions import Count

BALL_NAME = "INSERT_BALL_NAME_HERE"
players = await Player.annotate(
    ball_count=Count("balls", distinct=True)
).filter(ballsballcountry=BALL_NAME).order_by("-ball_count").limit(10)

print(BALL_NAME + "\n")
for player in players:
    discord_user = await bot.fetch_user(int(player.discord_id))
    print(f"{player.ball_count}: {discord_user}")
