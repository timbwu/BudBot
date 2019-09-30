import discord
from discord.ext import commands


# server commands
class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # bot on load
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game('CODE + ALGORITHMS'))
        print(f'{self.bot.user.name} has connected to Discord.')

    # member join server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    # member leave server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    # command permission
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have permission to use this command.')

    # ping command
    @commands.command(help='Ping the bot.')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    # kick member command
    @commands.command(help='Kick specified member.')
    @commands.has_role('Admin')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member}.')

    # ban member command
    @commands.command(help='Ban the specified user.')
    @commands.has_role('Admin')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}.')

    # unban member command
    @commands.command(help='Unban the specified user.')
    @commands.has_role('Admin')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}.')
                return

    # create channel command
    @commands.command(name='create-channel', help='Creates a new text channel')
    @commands.has_role('Admin')
    async def create_channel(self, res, channel_name):
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
    @commands.command(name='clear', help='Clears channel messages.')
    @commands.has_role('Admin')
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Management(bot))
