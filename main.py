import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_message_edit(before, after):
    await after.channel.send(f"wiadomość została edytowana z: {before.content}")
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#zdjęcia ----------------------------------------------------------------------------------
@bot.command()
async def mem(ctx):
    imgs = (os.listdir('images'))
    imgchan = random.randint(1,7)

    if imgchan == 1 or imgchan == 2 or imgchan == 3:
        img = (imgs)[0]
    elif imgchan == 4 or imgchan == 5:
        img = (imgs)[1]
    else:
        img = random.choice(imgs)
    with open(f'images/{img}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)    
bot.run("token")
