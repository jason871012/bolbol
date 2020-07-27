import discord
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension

with open('setting.json','r',encoding='utf8')as settingfile:
    settingdata=json.load(settingfile)

class React(Cog_Extension):

    @commands.command()
    async def pic(self,ctx):
        random_pic=random.choice(settingdata['pic'])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))