from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord import User
import time
import discord
import config
from models import Users, session
class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.rules = config.rules
        self.afk_users = {}
        self.rule_limited_users = {}
    @commands.has_permissions(ban_members=True)
    async def check_command(self, ctx, user: User):
        try:
            entry = await ctx.guild.fetch_ban(user)
            msg = f":hammer: Banned: Yes (Reason {entry.reason})\n"
        except discord.NotFound:
            msg = f":hammer: Banned: No\n"
        except discord.ext.commands.MissingPermissions:
            msg = f":hammer: Banned: Can't obtain status, 2FA is needed or I don't have permission!\n"
        except discord.errors.Forbidden:
            msg = f":hammer: Banned: Can't obtain status, 2FA is needed or I don't have permission!\n"
        userq = session.query(Users).filter_by(id=user.id).first()
        msg = msg + (f":triangular_flag_on_post: Strikes: {userq.strikes}")
        await ctx.send(msg)
        
    @cog_ext.cog_slash(name="check")
    async def check(self, ctx: SlashContext, user: User):
        await self.check_command(ctx, user)
    @commands.command(name="check")
    async def check_nonslash(self, ctx, user: User):
        await self.check_command(ctx, user)
    @commands.command()
    async def doihaveadmin(self, ctx):
        admin = ctx.message.guild.get_role(750596106400038932)
        if admin in ctx.author.roles:
            await ctx.send("Yes, you do!")
        else:
            await ctx.send("No, you don't.")
    async def rule_command(self,ctx,num):
        if not ctx.author in self.rule_limited_users or len(ctx.author.roles) != 1:
            self.rule_limited_users[ctx.author] = time.time()
            try:
                await ctx.send(self.rules[num])
            except KeyError:
                await ctx.send('That rule doesn\'t exist!')
        else:
            print('timed out')
            try:
                if time.time() - self.rule_limited_users[ctx.author] >= 5:
                    del self.rule_limited_users[ctx.author]
                    try:
                        await ctx.send(self.rules[num])
                    except KeyError:
                        await ctx.send('That rule doesn\'t exist!')
            except KeyError:
                try:
                    await ctx.send(self.rules[num])
                except KeyError:
                    await ctx.send('That rule doesn\'t exist!')
    @cog_ext.cog_slash(name="rule")
    async def rule(self, ctx: SlashContext, rule: int):
        await self.rule_command(ctx, rule)
    @commands.command(name="rule")
    async def rule_nonslash(self, ctx, rule: int):
        await self.rule_command(ctx, rule)
    @commands.has_permissions(ban_members=True)
    async def strike_command(self, ctx, user: discord.Member):
        userq = session.query(Users).filter_by(id=user.id).first()
        if userq == None:
            userq = Users(id=user.id, strikes=1, points=100)
        else:
            userq.strikes += 1
        session.add(userq)
        session.commit()
        await ctx.send("User has been struck!")
    @commands.command(name="strike")
    async def strike_standard(self, ctx, user: discord.Member):
        await self.strike_command(ctx, user)
    @cog_ext.cog_slash(name="strike")
    async def strike_slash(self, ctx, user: discord.Member):
        await self.strike_command(ctx, user)


def setup(bot):
    bot.add_cog(Moderation(bot))