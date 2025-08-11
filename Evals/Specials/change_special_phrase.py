from ballsdex.core.models import Special
from tortoise.exceptions import DoesNotExist

SPECIAL = "INSERT_NAME_OF_SPECIAL"
NEW_CATCH_PHRASE = "INSERT_NEW_CATCH_PHRASE"

try:
    special = await Special.get(name=SPECIAL)
except DoesNotExist:
    await ctx.send(f"The special '{SPECIAL}' does not exist.")
    return

erm = "`" * 3

try:
    special.catch_phrase = NEW_CATCH_PHRASE
    await special.save()
    await ctx.send(f"Successfully updated the catch phrase for '{SPECIAL}' to: {NEW_CATCH_PHRASE}")
except Exception as e:
    await ctx.send(
        f"Failed to update the catch phrase for '{SPECIAL}'.\n"
        f"{erm}\n{e}\n{erm}"
    )
    return
