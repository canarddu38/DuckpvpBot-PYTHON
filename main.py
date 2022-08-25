import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['DISCORD_TOKEN'])
