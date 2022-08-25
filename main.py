import discord
import os

help = """DuckSploit BOT - help
prefix: ```ds!```"""



class MyClient(discord.Client):
    async def on_ready(self):
        await bot.change_presence(activity=discord.Streaming(name="DuckSploit V1.0.8", url="https://ducksploit.com"))
    async def on_message(self, message):
        if message.content.startswith('ds!help'):
            await message.channel.send(help)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['DISCORD_TOKEN'])
