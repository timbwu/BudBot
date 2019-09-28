# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()  # client obj connection to discord

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Member dm
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, CODE AND ALGORITHMS BUD'
    )

# Member command response
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    randReply = [
        'Im number one',
        'FRANK',
        'Im a tree'
    ]

    if message.content == '!p':
        response = random.choice(randReply)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
