import asyncio
import discord

text = "MESSAGE HERE"

await ctx.send(text)

guilds = await GuildConfig.all()

for server in guilds:
    channel = bot.get_channel(server.spawn_channel)
    if channel:
        try:
            await channel.send(text)
            await asyncio.sleep(5)
        except discord.Forbidden:
            await ctx.send(f"Missing permissions for channel `{channel.id}`.")
        except discord.HTTPException as e:
            await ctx.send(f"HTTP error for channel `{channel.id}`: {e}")
        except Exception as e:
            await ctx.send(f"Unexpected error for channel `{channel.id}`: {e}")
    else:
        await ctx.send(f"Channel `{server.spawn_channel}` not found.")

await ctx.send("Done warning every server!")
