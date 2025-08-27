OLD_PLAYER = await Player.get(discord_id=INSERT_OLD_PLAYER_ID)
NEW_PLAYER, _ = await Player.get_or_create(discord_id=INSERT_NEW_PLAYER_ID)

await BallInstance.filter(player=OLD_PLAYER).update(player=NEW_PLAYER)
