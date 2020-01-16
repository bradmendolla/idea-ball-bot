import discord
import random
from config import TOKEN, GUILD, ROLE
from discord.ext import commands

bot = commands.Bot(command_prefix="!", case_insensitive = True)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and raring to go master!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the Bot Factory, {member.mention}! Await your instructions from The Handsome One!")
    role = discord.utils.get(guild.roles, name="Test Subjects")
    await bot.member.add_roles(member, role)




@bot.command(name="claptrap", help="Invokes Claptrap")
async def minion(ctx):
    clapback = ["Yes, master?", "Oh god...Stairs!", "Save me minion!"]


    response = random.choice(clapback)
    await ctx.send(response)

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
        if subject.status == users[0].status:
            online.append(subject)
    subject = random.choice(subjects)

    queries = ["do you want to be repeatedly shot full of questionable substances for very little test value? No response? Excellent!", "how do you feel about hypodermic uranium tattoos?", "I'm just gonna need you to hold still while I administer this harmless carcinogen." , "needs restraints! Hold them down!", "it says you requested electro shock treatments. I'm happy to oblige!"]
    question = random.choice(queries)
    await ctx.channel.send(f"{subject.mention} {question}")
    print(type(subject.status))
    print(len(online))
@bot.command(name="test")
async def test(ctx):
    roles = ctx.guild.roles
    author = ctx.author.roles
    users = ctx.guild.members
    subjects = []
    rando = random.choice(subjects)
    for user in users:
        if user.roles[1] == roles[2]:
            subjects.append(user)
    await ctx.channel.send(f"{roles[2]} {rando.roles[1]} {len(subjects)}")

bot.run(TOKEN)