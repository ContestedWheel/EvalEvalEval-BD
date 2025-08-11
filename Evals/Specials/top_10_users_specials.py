# Adjust the limit here.
# NOTE: The higher the limit, the slower the command works.
LIMIT = 10


players = {
    x.discord_id: await BallInstance.filter(special_id__isnull=False, player=x).count() for x in await Player.all()
}

sorted_players = sorted(players.items(), key=lambda count: count[1], reverse=True)

players = dict(sorted_players)

print("Special Leaderboard\n")

index = 1

for player, count in players.items():
    if index >= LIMIT + 1:
        break
    
    print(f"{index}. {await bot.fetch_user(player)} - {count}")

    index += 1
