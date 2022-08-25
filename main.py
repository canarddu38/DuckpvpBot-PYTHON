import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Streaming(name="DuckSploit V1.0.8", url="https://ducksploit.com"))
        print("Ready!")
    async def on_message(self, message):
        if message.content.startswith('ds!help'):
            embed=discord.Embed(title="DuckSploitBOT - help", description="""**help: ** ds!help""", color=0x00ff44)
            await message.channel.send(embed=embed)
        elif message.content.startswith('ds!test'):
            await message.channel.send("hey")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
