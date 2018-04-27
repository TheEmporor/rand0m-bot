import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix=".",description="heh.\n\nHelp Commands",owner_id=250674147980607488)

@bot.event
async def on_message(message):
    while True:
        await message.channel.send("js sucks lol")
        
        
bot.run('Mzg4NDc2MzM2Nzc3NDYxNzcw.DYgheQ.yW9j4XN1R5jABDcYFnTqeY9HzAQ')
        
        
        
