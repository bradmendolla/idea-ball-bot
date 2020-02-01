import discord
import random
from config import TOKEN, GUILD, ROLE
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="!", case_insensitive = True)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and raring to go master!")





#@bot.event
#async def on_member_join(member):
#    await member.create_dm()
#    
#    await member.dm_channel.send(f"Welcome to the Bot Factory, {member.mention}! Await your instructions from The Handsome One!")
    


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
    guild = ctx.guild
    channel = ctx.channel
    role = get(guild.roles, name="IdeaBall")
    users = role.members
    ballers = []
    for user in users:
        if user.status == "online":
            ballers.append(user)
        else:
            pass
    baller = random.choice(ballers)
    queries = ["do you want to be repeatedly shot full of questionable substances for very little test value? No response? Excellent!", "how do you feel about hypodermic uranium tattoos?", "I'm just gonna need you to hold still while I administer this harmless carcinogen." , "needs restraints! Hold them down!", "it says you requested electro shock treatments. I'm happy to oblige!"]
    question = random.choice(queries)
    #await channel.send(f"{baller.mention} {question}")
    
    try:
        await print(f"{len(ballers)} ")
    except TypeError:
        return


#test code to setup a role for idea ball

@bot.command()
async def setup(ctx):
    guild = ctx.guild
    channel = ctx.channel
    if get(guild.roles, name="IdeaBall"):
        await channel.send("Role Exists")
    else:
        await guild.create_role(name="IdeaBall")
    

#code to join role

@bot.command(name="join", help="Join IdeaBall role")
async def join(ctx):
    role = get(ctx.guild.roles, name="IdeaBall")
    user = ctx.message.author
    await user.add_roles(role)

#code to leave role
@bot.command(help="Leave IdeaBall role")
async def leave(ctx):
    role = get(ctx.guild.roles, name="IdeaBall")
    user = ctx.message.author
    await user.remove_roles(role)


bot.run(TOKEN)