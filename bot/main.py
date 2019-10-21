import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
bot = commands.Bot(command_prefix='$', description='A bot.')
client = discord.Client()
print('----------------------------------------------------------------------------')
print ("Discord.py API Version:")
print (discord.__version__)
print('----------------------------------------------------------------------------')
@client.event
async def on_ready():
    print('----------------------------------------------------------------------------')
    print("bot is up and running  User ID:")
    print(client.user)
    print('----------------------------------------------------------------------------')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)


@bot.command(name='list')
async def _list(ctx, arg):
    pass

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot", description="A bot.", color=0xeee657)

   
    embed.add_field(name="Author", value="Badbird 5907")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)
    
@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help",  value="Gives this message", inline=False)

    await ctx.send(embed=embed)


keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
