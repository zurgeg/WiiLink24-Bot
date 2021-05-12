from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord import User
import time
import discord
from models import Users, session
class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.rules = {
            1:"Use common sense! If you think it is wrong than don't post it!.",
            2:'No NSFW Content! No channels are marked as NSFW and there are people under 18 here.',
            3:'Keep advertising inside <#773219940647698462>',
            4:'Keep the chat in English.',
            5:'No drama! If you want to have drama, do it in DMs.',
            6:'Keep bot commands and other memes and other spammy stuff to <#750623633151492177>.',
            7:'No user bots. These are in some cases against the Discord ToS and if you need a bot for something use one of the bots already in the server.',
            8:"Don't send copyrighted content here, you can still talk about it though.",
            9:'MarioCube is the exception to above as the databases wad files are the only thing left of a lot of those apps and without them the apps would be lost to time.',
            10:'Don\'t attack anyone unless you have a valid reason to',
            11:'Only post junk in <#750623633151492177>',
            12:'People are people, no discrimination of any sort',
            13:'Do not ping staff unless needed',
            14:'Try to limit swearing',
            15:'Do not try to exploit the server though use of oversights in bots, leaked accounts etc.',
            24:'WiiConnect',
            418:'The requsted entity is short and stout.',
            9999:'You found a secret!'
        }
        self.afk_users = {}
        self.rule_limited_users = {}
    async def check_command(self, ctx, user: User):
        try:
            entry = await ctx.guild.fetch_ban(user)
            msg = f":hammer: Banned: Yes (Reason {entry.reason})\n"
        except discord.NotFound:
            msg = f":hammer: Banned: No\n"
        
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
        norole = "[<Role id=750581992223146074 name='@everyone'>]"
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
        user = session.query(Users).filter_by(id=user.id)
        user.strikes += 1
        session.add(user)
        session.commit()
    @commands.command(name="strike")
    async def strike_standard(self, ctx, user: discord.Member):
        await self.strike_command(ctx, user)

def setup(bot):
    bot.add_cog(Moderation(bot))