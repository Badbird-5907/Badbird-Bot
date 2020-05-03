#
import logging
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
logging.basicConfig(level=logging.INFO)
client = discord.Client()
nou = discord.Embed()
bot = commands.Bot(command_prefix='b!')
TOKEN = "fff"

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    print ("--------------------------------------------------------------")
    print ("Discord API version:")
    print (discord.version_info)
    print('Logged in as {0.user}'.format(client))
    print ("Token:")
    print (TOKEN)
    print ("--------------------------------------------------------------")
    await client.change_presence(activity=discord.Game(name='b!help'))
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Bot created by Badbird5897.", color=0xeee657)
    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link]https://bot.badbird5907.net")
    await ctx.send(embed=embed)
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Badbird Bot", description="Bot created by Badbird5897.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link]https://bot.badbird5907.net")
    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)
bot.run(TOKEN)
