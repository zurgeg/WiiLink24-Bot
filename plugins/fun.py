from discord.ext import commands
from random import randint
from discord_slash import cog_ext, SlashContext
import discord, datetime

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    async def dice_command(self, ctx, sides: int):
        await ctx.send(content=randint(1, sides))
    @commands.command(name="dice")
    async def dice_std(self, ctx, sides: int):
        await self.dice_command(ctx, sides)
    @cog_ext.cog_slash(name="dice")
    async def dice_slash(self, ctx: SlashContext, sides: int):
        await self.dice_command(ctx, sides)
    async def tables_command(self, ctx):
        embed = discord.Embed(title="Wii no Ma Tables", colour=discord.Colour(0xe956c9), timestamp=datetime.datetime.now())

        embed.set_image(url="https://cdn.discordapp.com/attachments/750623609810190348/842148517229232128/NEWTables.png")
        embed.set_author(name="HatSquid", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

        await ctx.send(embed=embed)
    @commands.command(name="tables")
    async def tables_std(self, ctx):
        await self.tables_command(ctx)
    @cog_ext.cog_slash(name="tables")
    async def tables_slash(self, ctx: SlashContext):
        await self.tables_command(ctx)
def setup(bot):
    bot.add_cog(Fun(bot))    
