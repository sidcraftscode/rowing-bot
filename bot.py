import discord
import os
from datetime import datetime

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

# List of messages to choose from
# get messages from workouts.txt
with open('workouts.txt', 'r') as file:
    MESSAGES = file.readlines()
    MESSAGES = [message.strip().replace('\\n', '\n') for message in MESSAGES]  # Replace "\n" with actual newlines
    

def get_next_index():
    try:
        with open('index.txt', 'r') as file:
            index = int(file.read().strip())
    except FileNotFoundError:
        index = 0
    except ValueError:
        index = 0
    return index

def save_index(index):
    with open('index.txt', 'w') as file:
        file.write(str(index))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Fetch channel by name
    channel_name = 'rowing-bot'
    for guild in client.guilds:
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel) and channel.name == channel_name:
                index = get_next_index()
                date = datetime.now().strftime('%d/%m')
                message = f":star: {date} - This week's workout is: \n " + MESSAGES[index]
                await channel.send(message)
                print(f"Sent message: {message}")
                
                # Update index to next message
                new_index = (index + 1) % len(MESSAGES)
                save_index(new_index)
                
                # Log out after sending the message
                await client.close()
                return

    print(f"Channel '{channel_name}' not found.")

# Token is set in the GitHub Actions environment
token = os.getenv('DISCORD_BOT_TOKEN')
client.run(token)
