import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

# We need more complex intents this time, we need to be able to access events related to members
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD) 
    print(f"{client.user} is online on {guild.name}!")
    
    general = discord.utils.get(guild.channels, name="general")
    await general.send(f"{client.user} is online on {guild.name}!")

@client.event
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name=GUILD)

    # Send a channel message
    general = discord.utils.get(guild.channels, name="general")
    await general.send(f"Hello {member.name}, welcome to {guild.name}!")

    # Send a DM
    await member.create_dm() # Create the DM room
    await member.dm_channel.send( # Send a DM
        f"Hello {member.name}, welcome to {guild.name}!"
    )

# Run the bot
client.run(TOKEN)