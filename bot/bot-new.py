#Badbird Bot BETA
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
TOKEN = ""

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
async def info(ctx):
    embed = discord.Embed(title="Badbird Bot", description="Bot created by Badbird5897.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Badbird 5907")
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
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'help':
        embed = discord.Embed(title="Commands", description="Here are some usefull commands:", color=0x00ff00)
        embed.add_field(name="b! uno-reverse", value="<red/blue/yellow/green>", inline=False)
        embed.add_field(name="b! ping", value="pong", inline=False)
        embed.add_field(name="b! roast-me", value="<will roast you>", inline=False)
        embed.add_field(name="say some swear words", value="<sh!t/fuc*>", inline=False)
        embed.add_field(name="say ok", value="<B00m3r>", inline=False)
        embed.add_field(name="say k", value="<k>", inline=False)
        embed.add_field(name="say f", value="<F>", inline=False)
        embed.add_field(name="say Die Badbird Bot", value="<a suprise>", inline=False)
        embed.add_field(name="And much more...", value="there is a lot more to be discoverd...",  inline=False)
        embed.add_field(name="Check out my website: https://badbird5907.net", value="https://badbird5907.net", inline=False)
        await message.channel.send(embed=embed)
            return

bot.run(TOKEN)
