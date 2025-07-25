# Inspect command originally named "info" made by Nixter and converted from CarFigures to Ballsdex by me.
# This command will send an embed with all of the information about the countryball (except for regime and economy).
# Make sure to import Ball as "from ballsdex.core.models import Ball"

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
        embed = discord.Embed(
            title=f"{emoji} {ball.country} Information:",
            description=(
                f"**⋄ Short Name:** {ball.short_name}\n"
                f"**⋄ Catch Names:** {''.join(ball.catch_names)}\n"
                f"**⋄ Rarity:** {ball.rarity}\n"
                f"**⋄ HP:** {ball.health}\n"
                f"**⋄ ATK:** {ball.attack}\n"
                f"**⋄ Capacity Name:** {ball.capacity_name}\n"
                f"**⋄ Capacity Description:** {ball.capacity_description}\n"
                f"**⋄ Credits:** {ball.credits}\n"
            ),
            color=discord.Colour.blurple()
        )
        await interaction.response.send_message(
            embed=embed
        )  # Send the ball information embed as a response
