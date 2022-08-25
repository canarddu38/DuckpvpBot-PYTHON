import discord
from discord import Webhook
import os
import requests
import aiohttp

class DSbot(discord.Client):
    def circle(pfp,size = (215,215)): 
        pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
        bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(pfp.size, Image.ANTIALIAS)
        mask = ImageChops.darker(mask, pfp.split()[-1])
        pfp.putalpha(mask)
        return pfp


    async def on_ready(self):
        await self.change_presence(activity=discord.Streaming(name="DuckSploit V1.0.8", url="https://ducksploit.com"))
        print("Ready!")


    async def on_member_join(member):
        guild = bot.get_guild(999999999999999) # <- Your Server (Guild) ID (Right-Click on Server Icon -> Copy ID)
        text = guild.get_channel(999999999999999) # <- Your Welcome-Channel ID (Right-Click on Text-Channel -> Copy ID)
        filename = "your-file.png" # <- The name of the file that will be saved and deleted after (Should be PNG)

        background = Image.open("welcome.png") # <- Background Image (Should be PNG)

        asset = member.avatar_url_as(size=1024) # This loads the Member Avatar
        data = BytesIO(await asset.read())

        pfp = Image.open(data).convert("RGBA")
        pfp = circle(pfp)
        pfp = pfp.resize((265,265)) # Resizes the Profilepicture so it fits perfectly in the circle

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("LemonMilkMedium-mLZYV.otf",42) # <- Text Font of the Member Count. Change the text size for your preference
        member_text = ("#" + str(guild.member_count) + "  USER") # <- Text under the Profilepicture with the Membercount
        draw.text((383,410),member_text,font=font)

        background.paste(pfp, (379,123), pfp) # Pastes the Profilepicture on the Background Image
        background.save(filename) # Saves the finished Image in the folder with the filename

        msg = await text.send(file = discord.File(filename),content ="WELCOME " + member.mention + "! Please read the rules! :heart:") # <- The welcome Message Content put above the Image. "member.mention" @mentions the user
        await asyncio.sleep(5) # 5 Seconds of waiting time
        try: 
            os.remove('C:/path/' + filename) # <- Change your path to where the Bot is located. Tries to delete the file again so your folder won't be full of Images. If it's already deleted nothing will happen
        except:
            pass


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
