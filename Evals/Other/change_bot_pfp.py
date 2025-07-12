import io
import discord

# Get the image from the message attachment
attachment = ctx.message.attachments[0] 
image_bytes = await attachment.read()

# Set the bot's profile picture
await bot.user.edit(avatar=image_bytes)
print("Bot profile picture updated successfully!")