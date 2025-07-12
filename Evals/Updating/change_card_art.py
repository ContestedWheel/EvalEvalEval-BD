COUNTRY = "country name here"  


from ballsdex.core.models import Ball
from ballsdex.packages.admin.cog import save_file
from ballsdex.settings import settings

from tortoise.exceptions import DoesNotExist

try:
  ball = await Ball.get(
    country = COUNTRY
  )
except DoesNotExist as e:
  await ctx.send("The country you have entered does not exist.")
  return

if ctx.message.attachments == []:
    await ctx.send("Please add an attached image to your eval message.")

image_attachment = ctx.message.attachments[0]

erm = ("`" * 3)

try:
    image_path = await save_file(image_attachment)
except Exception as e:
    await ctx.send(
        f"Attempt to change {settings.collectible_name}'s card art failed.\n"
        f"{erm}\n{e}\n{erm}"
    )
    return

ball.collection_card = "/" + str(image_path)

await ball.save()

await ctx.send(f"Successfully changed {ball.country}'s card art.")