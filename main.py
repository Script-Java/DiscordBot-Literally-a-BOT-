import discord
import requests as rq
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event

async def on_ready():
    print("Bot is online! logged in as" + " " + str(client.user))

async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return

@client.command()

async def randomNumber(ctx,max):
    # random number Generator
    try:
        number = random.randint(1,int(max))
        await ctx.send(f"Your random number is {number}!")
    except ValueError:
        await ctx.send(f"Please choose a Number not a Letter sped")

# Guessing age by name game
@client.command()

async def agify(ctx,name):
    request = rq.get(f"https://api.agify.io/?name={name}")
    response = request.json()
    embed = discord.Embed(
        title= "Api Agify.io",
        description= f"Agify is a Api that Tries guessing your age by your name \n"
                     f"```{name}``` age: {response['age']}"
                     f" \n request counts: {response['count']}",
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)

@client.command()
#help menu

async def helpMe(ctx):
    embed = discord.Embed(
        title= "Help Menu",
        description= "```!hello``` Says Hello"
                     "```!agify``` {name} Guesses your age by your name"
                     "```!randomNumber``` {max number you want it to generate``` generates number",
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)

@client.command()
#says Hi
async def hello(ctx):
    await ctx.send(f"Hello user")


client.run("OTg4OTQ3OTQ0MTI2NDI3MTU2.GRYhlF.hKDyUJXaYboW9cE-AmfU-Taox7dB-1LavwYRgc")
