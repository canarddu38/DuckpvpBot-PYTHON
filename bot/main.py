import os
from discord.ext import commands
import discord

TOKEN = os.environ("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True



class DSbot(discord.Client):
    async def on_ready():
       print(f"Logged in as {bot.user.name}({bot.user.id})")

    async def ping(ctx):
       await ctx.send("pong")

    
bot = DSbot(intents=intents)
bot.run(TOKEN)
