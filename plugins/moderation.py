from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord import Member 

class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    async def check_command(self, ctx, user: Member):
        await ctx.send("Work In Progress, sorry!")
    @cog_ext.cog_slash(name="check")
    async def check(self, ctx: SlashContext, user: Member):
        await self.check_command(ctx, user)
    @commands.command(name="check")
    async def check_nonslash(self, ctx, user: Member):
        await self.check_command(ctx, user)
        
def setup(bot):
    bot.add_cog(Moderation(bot))