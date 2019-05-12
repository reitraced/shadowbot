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

@client.command(pass_context=True, brief='Define Linux/UNIX terminology', description='Define terms, make sure to use commas to separate them. Ex. `shadowbot define linux, kernel`')
async def define(ctx, arg):
    if not arg:
        await ctx.send('You need to give me terms to define')
    else:
        terms = {
            "vim": "A common UNIX text editor. VI iMproved",
            "emacs": "A common UNIX text editor with an extensive scripting language called Lisp. Many variants with the most popular being GNU Emacs",
            "linux": "A family of computer operating systems using the Linux kernel.",
            "kernel": "The core of an operating system. Handles all inputs and outputs",
            "unix": "A standard for operating systems. Formerly one operating system that has since split. Here is a nice flow chart illustrating this split: https://upload.wikimedia.org/wikipedia/commons/7/77/Unix_history-simple.svg"
            "vi": "A text editor used on most older UNIX systems. Mostly replaced by Vim",
            "GNU": "The GNU Project is one of the largest FOSS projects in existence. It's software makes up the core of most Linux  operating systems"
        }

        answer = terms.get(arg)
        await ctx.send("The definition of " + arg + "is " + answer )


client.run(token)
