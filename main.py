import discord
from discord import Webhook
import os
import requests
import aiohttp

class DSbot(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Streaming(name="DuckSploit V1.0.8", url="https://ducksploit.com"))
        print("Ready!")
    async def on_message(self, message):
        if message.content.startswith('ds!help'):
            embed=discord.Embed(title="DuckSploitBOT - help", description="""```prefix: ds!
help: get commands list
versions: get lastest versions of DuckSploit
report: report a bug to our developpers
suggest: suggest an idea to our developpers```""", color=0x00ff44)
            await message.channel.send(embed=embed)
            
        elif message.content.startswith('ds!report'):
            async with aiohttp.ClientSession() as session:
                report = message.content.replace("ds!report ", "")
                print("New report: "+report)
                webhook = Webhook.from_url('https://discord.com/api/webhooks/970321539662753822/OVw73XELom6qvTGNCNpQfZVZ3Rz6gFWQNHCSYJXw0cAoaH9mh0Jx_mZUgLHIXpFOGgqf', session=session)
                embed = discord.Embed(title="New bug found", description="```"+report+"```")
                embed.add_field(name="Author", value=message.author)
                embed.color=0x00ff44
                await webhook.send(embed=embed)
            await message.channel.send("Your report is sended to our discord server. We'll fix it soon ;)")
            
        elif message.content.startswith('ds!versions'):
            response = requests.get(f"""https://raw.githubusercontent.com/canarddu38/DUCKSPLOIT/root/hacker/windows/version.txt""")
            version_windows = "Windows: "+response.text
            response = requests.get(f"""https://raw.githubusercontent.com/canarddu38/DUCKSPLOIT/root/hacker/linux/version.txt""")
            version_linux = "Linux: "+response.text
            response = requests.get(f"""https://raw.githubusercontent.com/canarddu38/DUCKSPLOIT/root/hacker/android/version.txt""")
            version_android = "Android: "+response.text
            
            embed = discord.Embed(title="DuckSploit lastest versions", description="```"+version_windows+"\n"+version_linux+"\n"+version_android+"```", color=0x00ff44)
            await message.channel.send(embed=embed)
            
        elif message.content.startswith('ds!suggest'):
            async with aiohttp.ClientSession() as session:
                suggest = message.content.replace("ds!suggest ", "")
                print("New suggestion: "+suggest)
                webhook = Webhook.from_url('https://discord.com/api/webhooks/1012380610985214042/3jQpTrxJdkg1N77xMuLhih6AdEModuJ9b798GnJ3WxlVkeZgv-AK77z0Cc9xCthzFWWk', session=session)
                embed = discord.Embed(title="New suggestion: ", description="```"+suggest+"```")
                embed.add_field(name="Author", value=message.author)
                embed.color=0x00ff44
                await webhook.send(embed=embed)
            await message.channel.send("Your suggestion is sended to our discord server. Maybe we'll add it soon ;)")
            
            
intents = discord.Intents.default()
intents.message_content = True
client = DSbot(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
