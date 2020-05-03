#Badbird Bot BETA
#--SETUP START--#
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
client = discord.Client()
bot = commands.Bot(command_prefix='b!')
TOKEN = ""
#--SETUP END--#
@client.event
async def on_ready():
    print("---Bot Info---")
    print("Discord API Version:", discord.version_info)
    print("Logged in as {0.user}".format(client))
    print("---Bot Info---")
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Badbird Bot", description="Bot created by Badbird5897.", color=0xeee657)
    # give info about you here
    embed.add_field(name="Author", value="Badbird 5907")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link]https://bot.badbird5907.net")
    await ctx.send(embed=embed)
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="Some Usefull commands", color=ff1100)
    embed.add_feild(name="b!help", value="shows this")
    embed.add_feild(name="test"),  value="test")
    await ctx.send(embed=embed)
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)
@bot.command()
async def say(ctx):
    await ctx.send(ctx)
@bot.command
async def unoreverse(ctx):
    if (ctx = red)
    elif (ctx = blue)
    elif (ctx = green)
bot.run(TOKEN)                          
