import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel=bot.get_channel(736245212724330587) 
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel=bot.get_channel(736245296610279454) 
    await channel.send(f'{member}leave!')

bot.run('NzM2MjMzOTU1MDA2NzQyNjYx.Xxr1TQ.PMA6_Zbh20uQVOu288Rs-7LwCzo')