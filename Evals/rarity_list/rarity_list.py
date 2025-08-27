async for rarity, country in Ball.filter(enabled=True).order_by("rarity").values_list("rarity", "country"):
    print(f"{rarity}. {country}")
