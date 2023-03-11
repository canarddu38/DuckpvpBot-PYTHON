import interactions
import discord
from discord import Webhook
import os
import requests
import aiohttp
import random

bot = interactions.Client(token=token)

#@bot.event
#async def on_ready():
	#await bot.change_presence(activity=discord.Streaming(name="V1.1", url="https://ducksploit.com"))

@bot.command(
    name="help",
    description="Get command list",
    scope=880882906350882817
)
async def help(ctx: interactions.CommandContext):
    embed=discord.Embed(title="DuckSploitBOT - help", description="""```prefix: /
help: get commands list
versions: get lastest versions of DuckSploit
report: report a bug to our developpers
suggest: suggest an idea to our developpers```""", color=0x00ff44)
    await ctx.send(embed=embed)
    
@bot.command(
	name="displayembed",
    description="Get command list",
    scope=880882906350882817
)
async def displayembed(ctx):
    embed = discord.Embed(title="Your title here", description="Your desc here") #,color=Hex code
    embed.add_field(name="Name", value="you can make as much as fields you like to")
    await ctx.send(embed=embed)
    
@bot.command(
    name="report",
    description="Report a bug to our team",
    scope=880882906350882817,
    options=[
        interactions.Option(
            name="description",
            description="Tell what is that bug",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def report(ctx: interactions.CommandContext, description: str):
    async with aiohttp.ClientSession() as session:
        report = description
        print("New report: "+report)
        webhook = Webhook.from_url('https://discord.com/api/webhooks/970321539662753822/pOVw73XELom6qvTGNCNpQfZVZ3Rz6gFWQNHCSYJXw0cAoaH9mh0Jx_mZUgLHIXpFOGgqfo', session=session)
        embed = discord.Embed(title="New bug found", description="```"+report+"```")
        embed.add_field(name="Author", value=message.author.name)
        embed.color=0x00ff44
        await webhook.send(embed=embed)
    await ctx.send("Your report is sended to our discord server. We'll fix it soon ;)")
    
    

            
@bot.command(
    name="version",
    description="Get DuckSploit's lastest versions",
    scope=880882906350882817
)
async def version(ctx: interactions.CommandContext):
    response = requests.get(f"""https://raw.githubusercontent.com/canarddu38/DUCKSPLOIT/root/hacker/windows/version.txt""")
    version_windows = "Windows: "+response.text
    response = requests.get(f"""https://raw.githubusercontent.com/canarddu38/DUCKSPLOIT/root/hacker/linux/version.txt""")
    version_linux = "Linux: "+response.text
    response = requests.get(f"""https://raw.githubusercontent.com/canarddu38/DUCKSPLOIT/root/hacker/android/version.txt""")
    version_android = "Android: "+response.text
            
    embed = discord.Embed(title="DuckSploit lastest versions", description="```"+version_windows+"\n"+version_linux+"\n"+version_android+"```", color=0x00ff44)
    await ctx.send(embed=embed)
            
        
        
        
@bot.command(
    name="suggest",
    description="Suggest a new feature to our team",
    scope=880882906350882817,
    options=[
        interactions.Option(
            name="description",
            description="Tell what is that improvement",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def report(ctx: interactions.CommandContext, description: str):
	async with aiohttp.ClientSession() as session:
		suggest = description
		print("New suggestion: "+suggest)
		webhook = Webhook.from_url('https://discord.com/api/webhooks/1012380610985214042/p3jQpTrxJdkg1N77xMuLhih6AdEModuJ9b798GnJ3WxlVkeZgv-AK77z0Cc9xCthzdFWWk', session=session)
		embed = discord.Embed(title="New suggestion: ", description="```"+suggest+"```")
		embed.add_field(name="Author", value=ctx.author.name)
		embed.color=0x00ff44
		await webhook.send(embed=embed)
	await ctx.send("Your suggestion is sended to our discord server. Maybe we'll add it soon ;)")

@bot.command(
    name="gend",
    description="End giveaway",
    scope=880882906350882817,
    options=[
        interactions.Option(
            name="message_id",
            description="id",
            type=interactions.OptionType.INTEGER,
            required=True
        ),
        interactions.Option(
            name="prize",
            description="prize",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def gend(ctx: interactions.CommandContext, message_id: int, prize: str):
	if ctx.author.guild_permissions.administrator:
		channel = ctx.get_channel(961337408375369768)
		message2 = await channel.fetch_message(message_id)



		users = set()
		for reaction in message2.reactions:
			async for user in reaction.users():
				users.add(user)
		winner = random.choice(tuple(users))
		embed = discord.Embed(title="🎊 | Giveaway Ended | 🎉", description="🎀 Thanks to all participants 🎀\nGg "+winner.mention+", you won "+prize+"\n```You can claim your prize by creating a ticket 🎫```")
		embed.set_footer(text="🎉┃Congrats")
		embed.color=0x00ff44

		msg = await message2.channel.send(embed=embed)
		await msg.add_reaction("🎊")  
		await msg.add_reaction("🎉")  
	else:
		ctx.send("✖️ error")
            
            
@bot.command(
    name="gcreate",
    description="Create giveaway",
    scope=880882906350882817,
    options=[
        interactions.Option(
            name="prize",
            description="prize",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def gcreate(ctx: interactions.CommandContext, prize: str):
	if message.author.guild_permissions.administrator:
		embed = discord.Embed(title=":tada: Giveaway! :tada:", description="Prize: "+prize+"\nHosted by "+ctx.author.mention)
		embed.set_footer(text="React with 🎉 for a chance to win '"+prize+"'")
		embed.color=0x00ff44
               
		channelid = ctx.get_channel(961337408375369768)
		msg = await channelid.send(embed=embed)
		await msg.add_reaction("🎉") 

		await ctx.send("Giveaway created :tada:")
	else:
		ctx.send("✖️ error")

bot.start()sage2.channel.send(embed=embed)
		await msg.add_reaction("🎊")  
		await msg.add_reaction("🎉")  
	else:
		ctx.send("✖️ error")
            
            
@bot.command(
    name="gcreate",
    description="Create giveaway",
    scope=880882906350882817,
    options=[
        interactions.Option(
            name="prize",
            description="prize",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def gcreate(ctx: interactions.CommandContext, prize: str):
	if message.author.guild_permissions.administrator:
		embed = discord.Embed(title=":tada: Giveaway! :tada:", description="Prize: "+prize+"\nHosted by "+ctx.author.mention)
		embed.set_footer(text="React with 🎉 for a chance to win '"+prize+"'")
		embed.color=0x00ff44
               
		channelid = ctx.get_channel(961337408375369768)
		msg = await channelid.send(embed=embed)
		await msg.a
