import discord
import random
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="!", case_insensitive = True)

#test to make
@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and raring to go master!")

# Test command

@bot.command(name="claptrap", help="Invokes Claptrap")
async def minion(ctx):
    clapback = ["Yes, minion?", "STAIRS? NOOOOOOOOOOOOOO!", "Save me minion!", "We've really come a long way, haven't we, minion?", "Let's get this party started!", "Glitching weirdness is a term of endearment, right?", "I AM GOING TO TEABAG YOUR CORPSE!", "Quick, minion, protect me with your face!", "Aaaand Open!", "Ah well -- now to slip back into the warm, comfy Christmas sweater that is my depression.", "Minion, what have you DONE?", "PROTECT ME, SQUIRE!", "Oh, SPHINCTERS!"]


    response = random.choice(clapback)
    await ctx.send(response)


# This is the code that tests the ideaball generator.
# It should only select people within a certain role
# who are also online.

@bot.command(name="playball", help="Summons an IdeaBall to be slammed into a random volunteer.")
async def playball(ctx):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    role = get(guild.roles, name="IdeaBall")
    users = role.members
    ballers = []
    for user in users:
        if user.status == discord.Status.online:
            ballers.append(user)
        else:
            pass
    ballers = [name for name in ballers if name != author]
    baller = random.choice(ballers)
    queries = ["do you want to play IdeaBall"]
    question = random.choice(queries)
    await channel.send(f"{baller.mention} {question}? {author.mention} wants to play.")
    


#code to setup a role for idea ball

@bot.command()
async def setup(ctx):
    guild = ctx.guild
    channel = ctx.channel
    if get(guild.roles, name="IdeaBall", color="#ffff33"):
        await channel.send("Role Exists")
    else:
        await guild.create_role(name="IdeaBall")
    

#code to join role

@bot.command(name="join", help="Join IdeaBall role")
async def join(ctx):
    channel = ctx.channel
    role = get(ctx.guild.roles, name="IdeaBall")
    user = ctx.message.author
    await user.add_roles(role)
    await channel.send(f"{user.mention} has joined the IdeaBall role. You are now willing to play IdeaBall with other people on the server.")

#code to leave role
@bot.command(name ="leave", help="Leave IdeaBall role")
async def leave(ctx):
    role = get(ctx.guild.roles, name="IdeaBall")
    user = ctx.message.author
    await user.remove_roles(role)
    await ctx.channel.send(f"{user.mention} has left the IdeaBall role. You are no longer willing to play IdeaBall with other people on the server.")

#command to check number of players
@bot.command(name="players", help="Check number of IdeaBallers online")
async def check_players(ctx):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    role = get(guild.roles, name="IdeaBall")
    users = role.members
    ballers = []
    for user in users:
        if user.status == discord.Status.online:
            ballers.append(user)
        else:
            pass
    ballers = [x for x in ballers if x != author]
    if len(ballers) != 1:
        await channel.send(f"There are {len(ballers)} IdeaBallers online that are not {author.mention}.")
    
    elif len(ballers) == 1:
        await channel.send(f"There is {len(ballers)} IdeaBaller online who is not {author.mention}.")

    else:
        await channel.send(f"There are no IdeaBallers online who aren't {author.mention}. Try again later.")

bot.run("NjY0MTg0NTE2MzIzMDQ5NDgy.XjXadw.ycSEEbxTKiPNd-jU08CJT8On8-s")