import random
from discord.ext import commands


# Fun commands
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # roll dice command
    @commands.command(help='Simulates rolling dice.')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    # talk command
    @commands.command(help='Responds with a random message.')
    async def talk(self, ctx):
        randText = [
            'Im one',
            'Im fast',
            'slow down boy',
        ]
        response = random.choice(randText)
        await ctx.send(response)

    # 8ball command
    @commands.command(help='Gives you an answer.')
    async def albert(self, ctx, *, question):
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
            'That will FAIL.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'No.',
            'Hahahaha...',
            'OK OK OK.',
            'Go pound sand.',
        ]
        await ctx.send(f'{random.choice(responses)}')


def setup(bot):
    bot.add_cog(Fun(bot))
