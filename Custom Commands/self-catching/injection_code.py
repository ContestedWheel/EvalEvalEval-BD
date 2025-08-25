# Copy them individually while adding them

# imports
import asyncio

# class variable
self.catch_by_itself = None

# main function
async def auto_catch():
    await asyncio.sleep(self.catch_by_itself)
    if not self.caught:
        bot_user = self.bot.user
        player = await Player.get(discord_id=bot_user.id)
        ball, is_new, dailycatch, fullsd = await self.catch_ball(
        bot_user, player=player, guild=channel.guild
        )
        await self.message.reply(
        self.get_catch_message(ball, is_new, bot_user.mention, dailycatch, fullsd),
        allowed_mentions=discord.AllowedMentions(users=player.can_be_mentioned),
        )
        await self.message.edit(view=self)

# trigger function
if self.catch_by_itself and type(self.catch_by_itself) == int:
  asyncio.create_task(auto_catch())
else:
  pass
