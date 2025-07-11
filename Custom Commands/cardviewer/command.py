
    # This is the viewcard command by AngerRandom.
    # This command sends the card of a countryball in ephemeral.
    # Uncomment the 4th app_commands if you want the command to be an admin command.
    @app_commands.command(name="viewcard", description="View a card of an existing countryball.")
    @app_commands.describe(brawler="The countryball to view card of")
    @app_commands.describe(special="Apply a sepcial to the card.")
    # @app_commands.checks.has_any_role(*settings.root_role_ids)
    async def viewcard(
        self,
        interaction: discord.Interaction["BallsDexBot"],
        countryball: BallTransform,
        special: SpecialTransform | None = None
    ):
        generator = CardGenerator(countryball, special)
        generator.special = special
        image, _ = generator.generate_image()

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

    # Send it as a Discord file
        discord_file = discord.File(fp=buffer, filename="card.png")
        try:
            await interaction.response.send_message(file=discord_file, ephemeral=True)
        except Exception as e:
            log.error("Something went wrong.", exc_info=e)
            await interaction.response.send_message("Something went wrong.", ephemeral=True)