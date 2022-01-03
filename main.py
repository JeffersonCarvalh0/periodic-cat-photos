import os

import discord
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise SystemExit("No valid token provided")

bot = commands.Bot(command_prefix="!pcats")
bot.load_extension("periodic_cats")
bot.run(token)
