from discord.ext import commands
from random import randint
from discord_slash import cog_ext, SlashContext

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    @cog_ext.cog_slash(name="dice")
    async def dice(self, ctx: SlashContext, sides: int):
        await ctx.send(content=randint(1, sides))
def setup(bot):
    bot.add_cog(Fun(bot))    
