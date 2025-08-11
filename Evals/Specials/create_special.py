NAME = "INSERT_NAME_OF_SPECIAL"


CATCH_PHRASE = "INSERT_CATCH_PHRASE"


START_DATE = "INSERT_STARTDATE(YYYY-MM-DD)"


END_DATE = "INSERT_ENDDATE(YYYY-MM-DD)"


EMOJI = "INSERT_EMOJI"


RARITY = INSERT_RARITY


TRADABLE = INSERT_True_OR_False


HIDDEN = INSERT_True_OR_False


from datetime import datetime
from ballsdex.packages.admin.balls import save_file


if ctx.message.attachments == []:
  await ctx.send("Please attach the card image to this message.")
  return

background = await save_file(ctx.message.attachments[0])

start = datetime.strptime(START_DATE, "%Y-%m-%d")
end =  datetime.strptime(END_DATE, "%Y-%m-%d")

m = "`" * 3

try:
    await Special.create(
        name=NAME,
        catch_phrase=CATCH_PHRASE,
        start_date=start,
        end_date=end,
        emoji=EMOJI,
        rarity=RARITY,
        background = "/" + str(background),
        tradeable=TRADABLE,
        hidden=HIDDEN
    )

    await ctx.send("Created a new event!")
except Exception as e:
    await ctx.send(
        "Failed to create event.\n"
        "Additional details displayed below:\n"
        f"{m}\n{e}\n{m}"
    )
    return
