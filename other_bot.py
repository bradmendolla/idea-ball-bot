import discord
import random
from config import TOKEN, GUILD, ROLE
from discord.ext import commands

bot = commands.Bot(command_prefix="!", case_insensitive = True)
role = client.Role
@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and raring to go master!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the Bot Factory, minion! Await your instructions from The Handsome One!")
    role = discord.utils.get(guild.roles, name="Test Subjects")
    await bot.member.add_roles(member, role)




@bot.command(name="claptrap", help="Invokes Claptrap")
async def minion(ctx):
    clapback = ["Yes, master?", "Oh god...Stairs!", "Save me minion!"]


    response = random.choice(clapback)
    await ctx.send(response)

@bot.command(name="playball", help="Summons an IdeaBall to be slammed into a random volunteer.")
async def playball(self, ctx):
    role = Role(name=ROLE)
    subjects = role.members
    selected = random.select(subjects)
    await ctx.channel.send(f"{selected} do you want to be repeatedly shot full of questionable substances for very little test value? No response? Excellent!")

bot.run(TOKEN)