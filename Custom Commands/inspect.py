# Inspect command originally named "info" made by Nixter and converted from CarFigures to Ballsdex by me.
# Thanks to arahman80 for making improvements to this command!
# This command will send an embed with all of the information about the countryball (except for regime and economy).

    @app_commands.command()
    @app_commands.checks.cooldown(1, 5, key=lambda i: i.user.id)
    async def inspect(self, interaction: discord.Interaction, ball: BallEnabledTransform):
        """
        Display info from a countryball without having the countryball.

        Parameters
        ----------
        ball: BallInstance
            The countryball you want to inspect
        """
        emoji = (
            self.bot.get_emoji(ball.emoji_id) or ""
        )  # Get emoji or an empty string if not found

        description_lines = []

        if ball.short_name:
            description_lines.append(f"**⋄ Short Name:** {ball.short_name}")

        if ball.catch_names:
            catch_names_str = ", ".join(name.strip() for name in ball.catch_names.split(";"))
            description_lines.append(f"**⋄ Catch Names:** {catch_names_str}")

        description_lines.extend([
            f"**⋄ Rarity:** {ball.rarity}",
            f"**⋄ HP:** {ball.health}",
            f"**⋄ ATK:** {ball.attack}",
            f"**⋄ Capacity Name:** {ball.capacity_name}",
            f"**⋄ Capacity Description:** {ball.capacity_description}",
            f"**⋄ Credits:** {ball.credits}",
        ])

        embed = discord.Embed(
            title=f"{emoji} {ball.country} Information:",
            description="\n".join(description_lines),
            color=discord.Colour.blurple()
        )
        await interaction.response.send_message(
            embed=embed
        )  # Send the ball information embed as a response
