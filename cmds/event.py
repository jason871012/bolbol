import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension

with open('setting.json','r',encoding='utf8')as settingfile:
    settingdata=json.load(settingfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel=self.bot.get_channel(int(settingdata['welcome'])) 
        await channel.send(f'{member}join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(int(settingdata['離開'])) 
        await channel.send(f'{member}leave!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith('apple')and msg.author != self.bot.user:
            await msg.channel.send('apple')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if 'good' in msg.content:
            await msg.channel.send('bad')
def setup(bot):
    bot.add_cog(Event(bot))