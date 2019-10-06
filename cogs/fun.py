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

    # 8ball command
    @commands.command(help='Gives you an answer.')
    async def albert(self, ctx, *, question):
        responses = [
            'NO, that will FAAAIL.',
            'This shit doesn\'t work.',
            'IS IT KLEEYAH WHAT IM TALKING ABOUT?',
            'YEEEAAAAS.',
            'NOOOOO.',
            'Hahahahahaha...',
            'OK OK OK OK.',
            'Go pound sand.',
        ]
        await ctx.send(f'{random.choice(responses)}')


def setup(bot):
    bot.add_cog(Fun(bot))
