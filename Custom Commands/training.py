# Originally made by newzac

    @app_commands.command()
    @app_commands.checks.cooldown(1, 10800, key=lambda i: i.user.id)
    async def training(self, interaction: discord.Interaction, countryball: BallInstanceTransform):
        """
        Start training to increase stats!
        """
        UserID = str(interaction.user.id)
        cb_txt = countryball.description(short=True, include_emoji=True, bot=self.bot)

        picker = random.randint(1,101)

        if picker >= 50:
            countryball.health_bonus += 1
            await countryball.save()
            
            await interaction.response.send_message(
                f"<@{UserID}> your **{cb_txt}** trained for a few minutes, causing its HP stat to increase by +1%!",
                ephemeral = False
            )

        else:
            countryball.attack_bonus += 1
            await countryball.save()

            await interaction.response.send_message(
                f"<@{UserID}> your **{cb_txt}** trained for a few minutes, causing its ATK stat to increase by +1%!",
                ephemeral = False
            )
        
        return
