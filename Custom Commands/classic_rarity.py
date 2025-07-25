# This is the classic rarity command made by GamingadlerHD.
# It is an embed rarity list, but it's not the rarity command from CarFigures.
# If you are looking for the rarity command from CarFigures, open "new_rarity.py" instead.

    @app_commands.command()
    @app_commands.checks.cooldown(1, 60, key=lambda i: i.user.id)
    async def rarity(self, interaction: discord.Interaction):
        # DO NOT CHANGE THE CREDITS TO THE AUTHOR HERE!
        """
        Show the rarity list of the dex - made by GamingAdlerHD
        """
        # Filter enabled collectibles
        enabled_collectibles = [x for x in balls.values() if x.enabled]

        if not enabled_collectibles:
            await interaction.response.send_message(
                f"There are no collectibles registered in {settings.bot_name} yet.",
                ephemeral=True,
            )
            return

        # Sort collectibles by rarity in ascending order
        sorted_collectibles = sorted(enabled_collectibles, key=lambda x: x.rarity)

        entries = []

        for collectible in sorted_collectibles:
            name = f"{collectible.country}"
            emoji = self.bot.get_emoji(collectible.emoji_id)

            if emoji:
                emote = str(emoji)
            else:
                emote = "N/A"
            # If you want the Rarity to only show full numbers like 1 or 12 use the code part here:
            # rarity = int(collectible.rarity)
            # otherwise you want to display numbers with decimals like 1.5, 5.3, 76.9 keep it as:
            # rarity = str(collectible.rarity)
            rarity = str(collectible.rarity)

            entry = (name, f"{emote} Rarity: {rarity}")
            entries.append(entry)
        # This is the number of countryballs who are displayed at one page, 
        # you can change this, but keep in mind: discord has an embed size limit.
        per_page = 7 

        source = FieldPageSource(entries, per_page=per_page, inline=False, clear_description=False)
        source.embed.description = (
            f"__**{settings.bot_name} rarity**__"
        )
        source.embed.colour = discord.Colour.blurple()
        source.embed.set_author(
            name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url
        )

        pages = Pages(source=source, interaction=interaction, compact=True)
        await pages.start()
