# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# command trigger
bot = commands.Bot(command_prefix='!')

# bot connected to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# random message
@bot.command(name='talk', help='Responds with a random message.')
async def gibb(res):
    randText = [
        'Im one',
        'Im fast',
        'slow down boy',
    ]
    response = random.choice(randText)
    await res.send(response)

# roll dice
@bot.command(name='rolldice', help='Simulates rolling dice.')
async def roll(res, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await res.send(', '.join(dice))


bot.run(token)
