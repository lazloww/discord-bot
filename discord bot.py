#Install Discord.py: Run pip install discord.py before executing the script.
import discord
from discord.ext import commands

# Configure intents
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True  # Required to track user activity in vc 

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_voice_state_update(member, before, after):
  
  
    # ya need to replace UR_ID with ur Discord user ID
    if member.id == UR_ID :
      
      
        # when ya join a vc 
        if after.channel and (before.channel != after.channel):
            channel = after.channel
            vc = discord.utils.get(bot.voice_clients, guild=member.guild)
            if not vc or not vc.is_connected():  
                await channel.connect()
                print(f"Joined {channel.name}")
        
      
        # if ya leave the vc 
        elif before.channel and not after.channel:
            vc = discord.utils.get(bot.voice_clients, guild=member.guild)
            if vc and vc.is_connected():
                await vc.disconnect()
                print("Disconnected")


# ya need to replace UR_TOKEN with ur Discord bot token from Discord Developer Portal.
bot.run('UR_TOKEN')
