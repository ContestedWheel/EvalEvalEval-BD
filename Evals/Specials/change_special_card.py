.eval 
from ballsdex.core.models import Special
from ballsdex.packages.admin.balls import save_file
from ballsdex.settings import settings
from tortoise.exceptions import DoesNotExist

SPECIAL = "SPECIAL_NAME"

try:
  special = await Special.get(
    name = SPECIAL
  )
except DoesNotExist as e:
  await ctx.send("The special you have entered does not exist.")
  return

if ctx.message.attachments == []:
    await ctx.send("Please add an attached image to your eval message.")

image_attachment = ctx.message.attachments[0]

erm = ("`" * 3)

try:
    image_path = await save_file(image_attachment)
except Exception as e:
    await ctx.send(
        f"Attempt to change {special.name}’s background failed.\n"
        f"{erm}\n{e}\n{erm}"
    )
    return

special.background = "/" + str(image_path)

await special.save()

await ctx.send(f"Successfully changed {special.name}’s background.")
