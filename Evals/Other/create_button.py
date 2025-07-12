class ButtonView(discord.ui.View):
   def init(self):
     super().init()

   @discord.ui.button(label="Text you want", style=discord.ButtonStyle.red)
   async def Prompt(self, interaction: discord.Interaction, Button: discord.ui.Button):
     await interaction.response.send_message(f"{interaction.user.mention} Text you want")

await ctx.send(view=ButtonView())