import discord
import random
from config import TOKEN, GUILD, ROLE
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="!", case_insensitive = True)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and raring to go master!")

@bot.event
async def on_message(message):
    print(f"Author: {message.author}, #{message.channel}")
    my_guild = bot.get_guild(GUILD)
    
    if message.content == "test":
        await message.channel.send(f"Wubwubwub")
    
    elif message.content == "roles":
        await print(f"{message.guild}")



@bot.event
async def on_member_join(member):
    await member.create_dm()
    
    await member.dm_channel.send(f"Welcome to the Bot Factory, {member.mention}! Await your instructions from The Handsome One!")
    


# Test command

@bot.command(name="claptrap", help="Invokes Claptrap")
async def minion(ctx):
    clapback = ["Yes, master?", "Oh god...Stairs!", "Save me minion!"]


    response = random.choice(clapback)
    await ctx.send(response)


# This is the code that tests the ideaball generator.
# It should only select people within a certain role
# who are also online.

@bot.command(name="playball", help="Summons an IdeaBall to be slammed into a random volunteer.")
async def playball(ctx):
    roles = ctx.guild.roles
    author = ctx.author.roles
    users = ctx.guild.members
    online = []
    subjects = []
    for user in users:
        if user.roles[1] == roles[2]:
            subjects.append(user)
    
    for subject in subjects:
        if subject.status == online:
            online.append(subject)
    subject = random.choice(subjects)

    queries = ["do you want to be repeatedly shot full of questionable substances for very little test value? No response? Excellent!", "how do you feel about hypodermic uranium tattoos?", "I'm just gonna need you to hold still while I administer this harmless carcinogen." , "needs restraints! Hold them down!", "it says you requested electro shock treatments. I'm happy to oblige!"]
    question = random.choice(queries)
    await ctx.channel.send(f"{subject.mention} {question}")
    
    print(len(users))
    print(len(online))


#test code to setup a role for idea ball

@bot.command()
async def setup(ctx):
    guild = ctx.guild
    await guild.create_role(name="IdeaBall")
    await print(f"Setup Triggered")

#code to join role

@bot.command(name="join", help="Join IdeaBall role")
async def join(ctx):
    role = get(ctx.guild.roles, name="IdeaBall")
    user = ctx.message.author
    await user.add_roles(role)


bot.run(TOKEN)