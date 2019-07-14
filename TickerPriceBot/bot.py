# Work with Python 3.6
import discord
import ticker_alert
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# @client.event
# async def on_ready():
#     print("The bot is ready!")
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def Price(ctx, ticker: str):
    await ctx.send(ticker_alert.callAPI(ticker))

@bot.command()
async def Add(ctx):
    await ctx.send("This command isn't implemented yet")

@bot.command()
async def List(ctx):
    await ctx.send("This command isn't implemented yet")

@bot.command()
async def All(ctx):
    await ctx.send("This command isn't implemented yet")

@bot.command()
async def Bot_quit(ctx):
    await bot.close()
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content == "Hello":
#         await message.channel.send(ticker_alert.callAPI())


TOKEN = open("token.txt", "r").read()
bot.run(TOKEN)