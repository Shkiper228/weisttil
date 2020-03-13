import discord
from discord.ext import commands


client = commands.Bot( command_prefix = '~')

@client.event

async def on_ready():
	print('login successfully completed')

@client.command( pass_context = True )

async def hello(ctx):
	await ctx.channel.send(ctx)

@commands.has_permissions(administrator = True)
@client.command(pass_context = True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

client.run('NjgxOTI5OTMxOTM2MzY2Njk2.XlVnZw.cXwQckSp5ROuWAKna5a8shk2w0c')