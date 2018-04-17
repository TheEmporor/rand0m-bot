import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix=".",description="heh.\n\nHelp Commands",owner_id=250674147980607488)

@bot.event
async def on_message(message):
    while True:
        await message.channel.send("@everyone")
        
        
bot.run('NDE5NDg1NjQwMjI5NTE5Mzcw.DXxAyw.9jOnRztt5gvO7gb70_HSBQ1Icy4')
        
        
        
