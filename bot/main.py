import os
from discord.ext import commands
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    @bot.event
    async def on_ready():
       print(f"Logged in as {bot.user.name}({bot.user.id})")

    @bot.command()
    async def ping(ctx):
       await ctx.send("pong")

    
intents = discord.Intents.default()
intents.message_content = True

bot = DSbot(intents)
bot.run(TOKEN)
