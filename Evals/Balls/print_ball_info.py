ball = await Ball.get(country="COUNTRY NAME")
print(f"=====Basic Information for {ball.country} =====")
print("===Object===")
print(f"Country: {ball.country}")
print(f"Ball id: {ball.id}")
print("===Names===")
print(f"Name: {ball.country}")
print(f"Short Name: {ball.short_name}")
print(f"Catch Names: {ball.catch_names}")
print("===Stats===")
print(f"Health: {ball.health}")
print(f"Attack: {ball.attack}")
print("===Compatability===")
print(f"Enabled: {ball.enabled}")
print(f"Tradeable: {ball.tradeable}")
print("===Extra Info===")
print(f"Rarity: {ball.rarity}")
print(f"Emoji ID: {ball.emoji_id}")
print(f"Credits: {ball.credits}")
print("===Ball Ability===")
print(f"Ability Name: {ball.capacity_name}")
print(f"Ability Description: {ball.capacity_description}")