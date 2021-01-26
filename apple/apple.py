import discord
from discord.ext import commands

class Apple(commands.Cog):
    """Reacts with a apple emoji if someone says apple."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'APPLE' in message.content.upper():
            await message.add_reaction('\N{APPLE}')

def setup(bot):
    bot.add_cog(Apple(bot))
