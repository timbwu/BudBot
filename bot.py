# bot.py
import os
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='talk', help='Responds with a random message')
async def gibb(mes):
    randText = [
        'Im one',
        'Im fast',
        'slow down boy',
    ]

    response = random.choice(randText)
    await mes.send(response)

bot.run(token)

