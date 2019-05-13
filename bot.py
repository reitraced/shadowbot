import discord
from discord.ext import commands

p = 'shadowbot '
client = commands.Bot(command_prefix=p)

f = open('token.txt', 'r')
token = f.read()
f.seek(0)
f.close()

f = open('game.txt', 'r')
lastgame = f.read()
f.seek(0)
f.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name=lastgame))

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(pass_context=True, brief='Define Linux/UNIX terminology', description='Define terms. Ex. `shadowbot define linux` Please use lowercase I am offended by capital latters.')
async def define(ctx, arg):
    if not arg:
        await ctx.send('You need to give me terms to define')
    else:
        f = open(arg + '.txt', 'r')
        answer = f.read()
        f.seek(0)
        f.close()

        await ctx.send("The definition of " + arg + " is: " + answer)


client.run(token)
