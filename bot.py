# bot.py
import os
import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# command trigger
bot = commands.Bot(command_prefix='!')
# status = cycle(['1', '2', '3'])


# bot ready
@bot.event
async def on_ready():
    # change_status.start()
    print(f'{bot.user.name} has connected to Discord.')


# error handling
# invalid command
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')


# background tasks
# @tasks.loop(seconds=7)
# async def change_status():
#     await bot.change_presence(activity=discord.Game(next(status)))


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
