NAME = "INSERT_REGIME_NAME"


import importlib
import os

from ballsdex.core.models import Regime

suffix = "balls" if os.path.isfile("ballsdex/packages/admin/balls.py") else "cog"
save_file = importlib.import_module(f"ballsdex.packages.admin.{suffix}").save_file

if ctx.message.attachments == []:
  await ctx.send("Please attach the card image to this message.")
  return

background = await save_file(ctx.message.attachments[0])

await Regime.create(name=NAME, background=f"/{background}")
await ctx.send("Created a new regime!")
