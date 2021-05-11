import config
from discord.ext import commands
from time import time
from discord_slash import SlashCommand

bot = commands.Bot()
slash = SlashCommand(bot, override_type = True, sync_commands=True)

print("Loading default extensions...")
start = time()

bot.load_extension("plugins.fun") 

end = time()
print(f"Loading default extensions took {end - start}ms")

bot.run(config.token)
