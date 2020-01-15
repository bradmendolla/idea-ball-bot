import os
import random
import discord
from config import TOKEN, GUILD
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hello minion! Welcome to the Bot Factory! Here, you will be subjected to dangerous, ill-advised, and humiliating procedures to refine more glorious bots! Exciting, isn't it?"
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    clapback = ["Minion! What did you want?", "Kinda busy right now.", "Wubwubwub"
        ]
    if message.content == "Claptrap!":
        response = random.choice(clapback)
        await message.channel.send(response)

    

client.run(TOKEN)