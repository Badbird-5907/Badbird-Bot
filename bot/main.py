import logging
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
logging.basicConfig(level=logging.INFO)
client = discord.Client()
nou = discord.Embed()
nou.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/030/219/uno.png")
TOKEN = "LMAO U TRIED B00M3R"

@client.event
async def on_ready():
    print ("Discord API version:")
    print (discord.version_info)
    print('Logged in as {0.user}'.format(client))
    print ("Token:")
    print (TOKEN)

print ("-------------------------------------------------------------")
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!help':
        await message.channel.send('Here are some commands:')
        await message.channel.send("!uno-reverse red,blue,green,yellow")
        await message.channel.send('ping')
        await message.channel.send('SHIT')


    if message.content == '!uno-reverse red':
            await message.channel.send(file=discord.File('images/images/unored.png'))

    if message.content == '!uno-reverse blue':
                    await message.channel.send(file=discord.File('images/images/unoblue.png'))

    if message.content == '!uno-reverse green':
                    await message.channel.send(file=discord.File('images/images/unogreen.png'))

    if message.content == '!uno-reverse yellow':
                    await message.channel.send(file=discord.File('images/images/unoyellow.png'))

    if message.content == 'ping':
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
                        await channel.send(file=discord.File('images/images/nou.png'))


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
