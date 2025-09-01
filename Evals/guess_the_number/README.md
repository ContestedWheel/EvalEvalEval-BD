> [!NOTE]  
> This eval was made by [AngerRandom](https://github.com/AngerRandom), I just made a easy to follow tutorial with markdown.

# How do I run this?

1. Download the `guessthenumbertemplate.py` file. Open the file in your text editor of choice.

2. Replace the following in the code:

- `CHANNEL_ID`: Replace this with the Discord channel ID of your choice. Developer Mode needs to be turned on in User Settings to obtain this, click [here](https://discord.com/developers/docs/activities/building-an-activity#step-0-enable-developer-mode) to learn how.

- `SPAWN_AMOUNT`: Replace this with the number of balls you want the bot to spawn if a correct guess is made. It is adviced to limit this number to 100 to avoid your bot getting rate limited.

> [!TIP]
> Optionally, you also can set the log channel in config so that the bot sends the answer privately.

Here is an example of what replacing both of these look like:

<img width="472" height="144" alt="image" src="https://github.com/user-attachments/assets/3eba90dd-756c-4f66-b720-02349291d9d5" />

3. Save your changes in the file, then run this eval below:
```py
content = await message.attachments[0].read()

await ctx.invoke(bot.get_command("eval"), body=content.decode())
```

Make sure you attach the file along with the eval, otherwise it will not work. Visual example is shown below:

<img width="608" height="555" alt="image" src="https://github.com/user-attachments/assets/e00d87f1-08bb-4ab0-ba40-f3cb4f943553" />
