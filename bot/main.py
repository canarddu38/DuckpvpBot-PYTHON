import os
from discord.ext import commands

bot = commands.Bot(command_prefix="db!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    ctx.send("pong")
    
def ping2(ctx):
    ctx.send("pong2")

if __name__ == "__main__":
    bot.run(TOKEN)
