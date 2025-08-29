from ballsdex.core.models import Ball

class CatchView(discord.ui.View):
    def init(self):
        super().init(timeout=None)

    @discord.ui.button(label="button message here", style=discord.ButtonStyle.blurple)
    async def catchme(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message(f"{interaction.user.mention} message here")

Ball = await Ball.get(country="countryball name here")
file_location = "./admin_panel/media/" + Ball.wild_card
channel = bot.get_channel(channel id here)
await channel.send("spawn message here", file=discord.File(file_location), view=CatchView())
