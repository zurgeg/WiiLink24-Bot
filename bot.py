import config
import discord
from discord.ext import commands
from time import time
from discord_slash import SlashCommand
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intents)
slash = SlashCommand(bot, override_type = True, sync_commands=True)

print("Loading default extensions...")
start = time()

bot.load_extension("plugins.fun") 
# bot.load_extension("plugins.moderation") 

end = time()
print(f"Loading default extensions took {end - start}ms")

bot.run(config.token)
