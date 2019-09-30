# bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# command trigger
bot = commands.Bot(command_prefix='!')

# load extension command
@bot.command(help='Loads an extension.')
@commands.has_role('Admin')
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

# unload extension command
@bot.command(help='Unloads an extension.')
@commands.has_role('Admin')
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

# check for cogs on start
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
