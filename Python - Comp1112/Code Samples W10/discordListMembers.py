import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD") # Load the guild from the env file

# Create discord client
client = discord.Client(intents=discord.Intents.default())

@client.event 
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD) # In case we are connected to multiple guilds, we can select the active guild with our env file
    print(f"{client.user} is online on {guild.name}!")
    members = ""
    for member in guild.members:
        members += "\n - " + member.name
    print("Current members are:" + members)

# Run the bot
client.run(TOKEN)