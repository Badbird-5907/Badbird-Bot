import logging
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
client = discord.Client()
nou = discord.Embed()
nou.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/030/219/uno.png")
TOKEN = "noI"

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

guilds = len([s for s in client.guilds])
print (guilds)
@client.event
async def on_ready():
    print ("--------------------------------------------------------------")
    print ("Discord API version:")
    print (discord.version_info)
    print('Logged in as {0.user}'.format(client))
    print ("Token:")
    print (TOKEN)
    print ("--------------------------------------------------------------")
    await client.change_presence(activity=discord.Game(name='help | badbird5907.net'))

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

    if message.content.startswith('b! roast-me'):
            await message.channel.send('I was told not to roast trash because it smells like SH!T')

    if message.content == 'b! uno-reverse':
            await message.channel.send('Please use the command b! uno-reverse <colour (red/blue/green/yellow)>')

    if message.content == 'b! uno-reverse red':
            await message.channel.send(file=discord.File('images/images/unored.png'))

    if message.content == 'b! uno-reverse blue':
                    await message.channel.send(file=discord.File('images/images/unoblue.png'))
    if message.content == 'b! uno-reverse green':
                    await message.channel.send(file=discord.File('images/images/unogreen.png'))

    if message.content == 'b! uno-reverse yellow':
                    await message.channel.send(file=discord.File('images/images/unoyellow.png'))

    if message.content == 'b! ping':
        await message.channel.send('pong')

    if message.content == 'SHIT':
            await message.channel.send(file=discord.File('images/gif/rhinopoo.gif'))

    if message.content == 'Shit':
            await message.channel.send(file=discord.File('images/gif/rhinopoo.gif'))
    if message.content == 'shit':
                    await message.channel.send(file=discord.File('images/gif/rhinopoo.gif'))
   
    if message.content == 'DIE Badbird Bot':
                await message.channel.send('NOU')
                await message.channel.send('UNO REVERSE')
                await message.channel.send(file=discord.File('images/images/nou.png'))

    if message.content == 'die badbird bot':
                        await message.channel.send('NOU')
                        await message.channel.send('UNO REVERSE')
                        await message.channel.send(file=discord.File('images/images/nou.png'))

    if message.content == 'Die badbird bot':
                        await message.channel.send('NOU')
                        await message.channel.send('UNO REVERSE')
                        await message.channel.send(file=discord.File('images/images/nou.png'))


    if message.content == 'die Badbird Bot':
                        await message.channel.send('NOU')
                        await message.channel.send('UNO REVERSE')
                        await message.hannel.send(file=discord.File('images/images/nou.png'))


    if message.content == 'DIE BADBIRD BOT':
                        await message.channel.send('NOU')
                        await message.channel.send('UNO REVERSE')
                        await message.channel.send(file=discord.File('images/images/nou.png'))

    if message.content.startswith('Stop'):
        await message.channel.send('NO!')

    if message.content.startswith('stop'):
        await message.channel.send('NO!')
    if message.content.startswith('STOP'):
        await message.channel.send('NO!')
      
    if message.content.startswith('STAHP'):
        await message.channel.send('NO!')

    if message.content.startswith('stahp'):
        await message.channel.send('NO!')

    if message.content.startswith('Stahp'):
        await message.channel.send('NO!')

    if message.content.startswith('Sthap'):
        await message.channel.send('NO!')

    if message.content.startswith('STHAP'):
        await message.channel.send('NO!')

    if message.content.startswith('sthap'):
        await message.channel.send('NO!')

    if message.content.startswith('k'):
        await message.channel.send('k')
    
    if message.content.startswith('K'):
        await message.channel.send('k')

    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('Hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('HI'):
        await message.channel.send('Hello!')

    if message.content.startswith('f'):
        await message.channel.send('F')

    if message.content.startswith('F'):
        await message.channel.send('F')

    if message.content.startswith('lol'):
        await message.channel.send('LMAO')

    if message.content.startswith('LOL'):
        await message.channel.send('LMAO')
    if message.content.startswith('Lol'):
        await message.channel.send('LMAO')

    if message.content.startswith('lmao'):
        await message.channel.send('LMAO!')

    if message.content.startswith('LMAO'):
        await message.channel.send('LMAO!')

    if message.content.startswith('Lmao'):
        await message.channel.send('LMAO!')

    if message.content.startswith('lmao'):
        await message.channel.send('LMAO!')

    if message.content.startswith('ok'):
        await message.channel.send('B00m3r')

    if message.content.startswith('Ok'):
        await message.channel.send('B00m3r')

    if message.content.startswith('OK'):
        await message.channel.send('B00M3R')
    
    if message.content.startswith('fuck'):
        await message.channel.send('Calm Down B00M3R')

    if message.content.startswith('Fuck'):
        await message.channel.send('Calm Down B00M3R')

    if message.content.startswith('FUCK'):
        await message.channel.send('Calm Down B00M3R')
client.run(TOKEN)
