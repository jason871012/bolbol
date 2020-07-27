import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import datetime

with open('setting.json','r',encoding='utf8')as settingfile:
    settingdata=json.load(settingfile)

class ig(Cog_Extension):

    @commands.command()
    async def ig(self,ctx):
        embed=discord.Embed(title="YouTube", url="https://www.youtube.com/feed/subscriptions", description="這是IG", color=0x3bde4e,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Instagram", url="https://www.instagram.com/?hl=zh-tw", icon_url="https://imgur.com/wxxB7tm.jpg")
        embed.set_thumbnail(url="https://imgur.com/mlU0U1a.gif")
        embed.add_field(name="aa", value="11", inline=True)
        embed.add_field(name="bb", value="22", inline=True)
        embed.add_field(name="cc", value="33", inline=True)
        embed.add_field(name="dd", value="44", inline=True)
        embed.set_footer(text="結束囉")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ig(bot))