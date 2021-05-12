import config
import discord
from discord.ext import commands
from time import time
from discord_slash import SlashCommand
from sqlalchemy import create_engine

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intents)
slash = SlashCommand(bot, override_type = True, sync_commands=True)

print("Loading default extensions...")
start = time()

bot.load_extension("plugins.fun") 
bot.load_extension("plugins.moderation") 

end = time()
print(f"Loading default extensions took {end - start}s")

print("Loading community extensions")
start = time()

for plugin in config.plugins:
  bot.load_extension(plugin)

end = time()
print(f"Loading community extensions took {end - start}s")

bot.run(config.token)
