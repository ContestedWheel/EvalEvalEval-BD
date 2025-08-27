specials = {x: 0 for x in await Special.all().values_list("name", flat=True)}

async for ball in BallInstance.filter(special_id__isnull=False).prefetch_related("special"):
    specials[ball.special.name] += 1

sorted_specials = sorted(specials.items(), key=lambda count: count[1], reverse=True)

specials = dict(sorted_specials)

print("Special Counts\n\n")

index = 1

for special, count in specials.items():
    print(f"{index}. {special} - {count}")

    index += 1
