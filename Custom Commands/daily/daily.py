# Imports
import json
import os
import random
import traceback
from datetime import datetime, timedelta, timezone
from ballsdex.packages.countryballs.countryball import BallSpawnView
# Paste this on line 39
TIMEZONE_SETTING = timezone(timedelta(hours=8)) # Timezone configuration - change this to adjust timezone

# Paste this on line 124
        self.daily_claims = {}
        self.daily_claims_file = os.path.join(os.path.dirname(__file__), "daily_claims.json")
        self.load_daily_claims()
    
    def load_daily_claims(self):
        """Load daily claim records"""
        if os.path.exists(self.daily_claims_file):
            try:
                with open(self.daily_claims_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for user_id, timestamp in data.items():
                        if isinstance(timestamp, str):
                            dt = datetime.fromisoformat(timestamp)
                            if dt.tzinfo is None:
                                dt = dt.replace(tzinfo=TIMEZONE_SETTING)
                            self.daily_claims[int(user_id)] = dt
                        else:
                            dt = datetime.fromtimestamp(timestamp, tz=TIMEZONE_SETTING)
                            self.daily_claims[int(user_id)] = dt
            except Exception as e:
                print(f"Error occurred while loading daily claim records: {str(e)}")
                self.daily_claims = {}
                self.save_daily_claims()

    def save_daily_claims(self):
        """Save daily claim records"""
        try:
            data = {str(uid): ts.isoformat() for uid, ts in self.daily_claims.items()}
            with open(self.daily_claims_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error occurred while saving daily claim records: {str(e)}")


# The actual command. Paste this anywhere or on a new line at the end of the file.
    @app_commands.command()
    @app_commands.guild_only()
    async def daily(self, interaction: discord.Interaction):
        """
        Daily check-in to claim rewards.
        """
        await interaction.response.defer(thinking=True)
        
        user_id = interaction.user.id
        now = datetime.now(TIMEZONE_SETTING)
        
        if user_id in self.daily_claims:
            last_claim = self.daily_claims[user_id]
            if last_claim.tzinfo is None:
                last_claim = last_claim.replace(tzinfo=TIMEZONE_SETTING)
            
            today_midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
            if last_claim >= today_midnight:
                next_midnight = today_midnight + timedelta(days=1)
                time_left = next_midnight - now
                hours = int(time_left.total_seconds() // 3600)
                minutes = int((time_left.total_seconds() % 3600) // 60)
                await interaction.followup.send(
                    f"You have already claimed today's reward!\n"
                    f"Please try again in {hours} hours and {minutes} minutes.",
                    ephemeral=True
                )
                return
                
        player, _ = await Player.get_or_create(discord_id=user_id)
            
        try:
            spawn_view = await BallSpawnView.get_random(self.bot)
            ball = spawn_view.model
            
            instance = await BallInstance.create(
                ball=ball,
                player=player,
                attack_bonus=random.randint(-settings.max_attack_bonus, +settings.max_attack_bonus),
                health_bonus=random.randint(-settings.max_health_bonus, +settings.max_health_bonus),
            )
            
            self.daily_claims[user_id] = now
            self.save_daily_claims()
            
            content, file, view = await instance.prepare_for_message(interaction)
            file.filename = "daily_card.png"
            
            embed = discord.Embed(
                title="🎁 Daily Check-in Reward",
                description=f"Congratulations on claiming your daily reward!\nYou received: {ball.country} (ATK:{instance.attack} HP:{instance.health})",
                color=discord.Color.green()
            )
            embed.set_image(url="attachment://daily_card.png")
            
            await interaction.followup.send(embed=embed, file=file)
            
        except Exception as e:
            print(f"Error occurred while distributing daily reward: {str(e)}")
            traceback.print_exc()
            await interaction.followup.send(
                "An error occurred while distributing the reward. Please try again later!",
                ephemeral=True
            )
