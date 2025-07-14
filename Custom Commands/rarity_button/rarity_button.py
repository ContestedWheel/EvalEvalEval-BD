    @button(style=discord.ButtonStyle.success, label="Rarity")
    async def rar_btn(self, interaction: discord.Interaction["BallsDexBot"], button: Button):
        await interaction.response.send_message(
            f"The rarity of this ball is: {self.model.rarity}",
            ephemeral=True,
        )
