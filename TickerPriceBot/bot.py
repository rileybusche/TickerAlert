# Work with Python 3.6
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

TOKEN = 'NTk5NjE5NTYzNzU5NTk5NjU4.XSn2aA.fZG5nBZPX06puUccnbDYDusgkdg'
client.run(TOKEN)