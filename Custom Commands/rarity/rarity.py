# You should have defaultdict imported before you put this command in your bot. If not, put this below "from typing import TYPE_CHECKING, cast"
from collections import defaultdict

# Command to put in your bot:
    @app_commands.command()
    @app_commands.describe(countryball="The ball to be queried")
    async def rarity(
        self,
        interaction: discord.Interaction["BallsDexBot"],
        countryball: BallEnabledTransform | None = None,
    ):
        """
        rarity list for balls, grouped by rarity level, or search for the rarity of a specific ball.

        Parameters
        ----------
        countryball: Ball
            Optional: Check the rarity of a specific ball
        """
        await interaction.response.defer(thinking=True)
        if countryball:
            emoji = self.bot.get_emoji(countryball.emoji_id) or ""
            embed = discord.Embed(
                title=f"Rarity of {countryball.country}",
                description=f"{emoji} {countryball.country}\nRarity: {countryball.rarity}",
                color=discord.Color.blurple(),
            )
            await interaction.followup.send(embed=embed, ephemeral=False)
            return
        balls_list = [ball for ball in balls.values() if ball.enabled]
        balls_list.sort(key=lambda b: (b.rarity, b.country))
        rarity_map = defaultdict(list)
        for ball in balls_list:
            rarity_map[ball.rarity].append(ball)
        rarity_keys = sorted(rarity_map.keys())
        page_size = 5 # change this to adjust number of rarities per page
        pages = []
        for i in range(0, len(rarity_keys), page_size):
            page_rarities = rarity_keys[i:i+page_size]
            desc = ""
            for rarity in page_rarities:
                desc += f"▌Rarity: {rarity}\n"
                for ball in rarity_map[rarity]:
                    emoji = self.bot.get_emoji(ball.emoji_id) or ""
                    desc += f"{emoji} {ball.country}\n"
                desc += "\n"
            pages.append(desc.strip())
        from ballsdex.core.utils import menus
        class RarityPageSource(menus.ListPageSource):
            def __init__(self, pages):
                super().__init__(pages, per_page=1)
            async def format_page(self, menu, page):
                embed = discord.Embed(title="Rarity List", color=discord.Color.blurple())
                embed.description = page
                return embed
        source = RarityPageSource(pages)
        paginator = Pages(source=source, interaction=interaction, compact=True)
        await paginator.start()
