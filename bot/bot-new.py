import logging
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
logging.basicConfig(level=logging.INFO)
client = discord.Client()
nou = discord.Embed()
bot = commands.Bot(command_prefix='!')
TOKEN = "fff"

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
async def foo(ctx, arg):
    await ctx.send(arg)
    
