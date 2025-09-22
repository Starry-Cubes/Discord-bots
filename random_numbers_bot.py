import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, I am {bot.user}!')

@bot.command()
async def roll_die(ctx, die: int, amount = 1):
    with open("rolls.txt", mode = 'a+') as x:
        finalRolls = ""
        for i in range(amount):
            result = random.randint(1, die)
            finalRolls += str(result) + "\n"
            x.write(f"From {die} got {result}, rolled by: {ctx.author.name} \n")
        await ctx.send(finalRolls)

@bot.command()
async def search_rolls(ctx, search: str):
    result = ""
    with open("rolls.txt", mode = 'r') as x:
        r = x.readlines()
    for i in range(len(r)):
        if search in r[i]:
            result += str(r[i]) + "on line: " + str(i + 1) + "\n"
    if result == "":
        result = "there was no such thing in the file"
    await ctx.send(result)  

@bot.command()
async def all_rolls(ctx):
    print("hi")
    with open("rolls.txt", mode = 'rb') as x:
        f = discord.File(x)
    await ctx.send(file=f)


@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

bot.run(token)
