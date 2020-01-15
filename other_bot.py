import discord
import random
from config import TOKEN, GUILD
from discord.ext import commands

bot = commands.Bot(command_prefix="!", case_insensitive = True)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and raring to go master!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the Bot Factory, minion! Await your instructions from The Handsome One!")
    role = discord.utils.get(guild.roles, name="Test Subjects")
    await bot.member.add_roles(member, role)

@bot.event
async def on_member_leave(member):
    await member.create_dm()
    await member.dm_channel.send(f"You have been kicked from the Bot Factory {member.mention}. This may have been done automatically, or the Handsome one wishes to test something on you personally. An invite back to the server shall be forthcoming.")


@bot.command(name="claptrap", help="Invokes Claptrap")
async def minion(ctx):
    clapback = ["Yes, master?", "Oh god...", "Save me minion!"]

    response = random.choice(clapback)
    await ctx.send(response)


@bot.command(name="ideaball")
#define function
async def ideaball(ctx):
#select user
    await discord.User

bot.run(TOKEN)