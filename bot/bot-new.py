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
@bot.command(name+'help')
async def help():
    await send(
    embed=discord.Embed(title="Commands", description="Some usefull commands", color=0x00ff00)
    embed.set_author(name="a")
    embed.add_field(name="a", value="undefined", inline=False)
    await self.bot.say(embed=embed)
    )
bot.run(TOKEN)
