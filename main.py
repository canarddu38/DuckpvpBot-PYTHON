import discord
import os

help = """DuckSploit BOT - help
prefix: ```ds!```"""



class MyClient(discord.Client):
    async def on_ready(self):
        print("Ready!")
    async def on_message(self, message):
        if message.content.startswith('ds!help'):
            await message.channel.send(help)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['DISCORD_TOKEN'])
