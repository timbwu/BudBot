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

# member join server
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

# member leave server
@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# command permission
@bot.event
async def on_command_error(res, error):
    if isinstance(error, commands.errors.CheckFailure):
        await res.send('You do not have permission to use this command.')

# ping command
@bot.command(name='ping', help='Pings the bot')
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# kick member command
@bot.command()
@commands.has_role('Admin')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member}.')

# ban member command
@bot.command()
@commands.has_role('Admin')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}.')

# unban member command
@bot.command()
@commands.has_role('Admin')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}.')
            return

# create channel command
@bot.command(name='create-channel', help='Creates a new text channel')
@commands.has_role('Admin')
async def create_channel(res, channel_name):
    guild = res.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        await res.send('{.mention} created!'.format(discord.utils.get(guild.channels, name=channel_name)))
    else:
        print(f'Channel already exists')
        await res.send('{.mention} channel already exists'.format(existing_channel))

# clear messages command
@bot.command(name='clear', help='Clears channel messages.')
@commands.has_role('Admin')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# talk command
@bot.command(name='talk', help='Responds with a random message.')
async def gibb(res):
    randText = [
        'Im one',
        'Im fast',
        'slow down boy',
    ]
    response = random.choice(randText)
    await res.send(response)

# roll dice command
@bot.command(name='roll-dice', help='Simulates rolling dice.')
async def roll(res, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await res.send(', '.join(dice))

# 8ball command
@bot.command(name='albert', help='Gives you an answer.')
async def albert(ctx, *, question):
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook is not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'No.',
        'Yes, definitely.',
        'You may rely on it.',
        'Go pound sand.',
    ]
    await ctx.send(f'{random.choice(responses)}')


bot.run(token)
