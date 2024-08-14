import discord
import os
import json

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

# Define a list of messages
messages = [
    "Hello there!",
    "Hope you're having a great week!",
    "Remember to stay positive!",
    "Keep up the good work!",
    "Don't forget to take breaks!",
]

# Define a file to keep track of the last sent message
message_index_file = "message_index.json"

def get_message_index():
    # Load the last index used from the file
    if os.path.exists(message_index_file):
        with open(message_index_file, 'r') as f:
            return json.load(f).get('index', 0)
    return 0

def update_message_index(index):
    # Save the current index to the file
    with open(message_index_file, 'w') as f:
        json.dump({'index': index}, f)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Get the current index
    index = get_message_index()

    # Send the message from the list
    channel = discord.utils.get(client.get_all_channels(), name='rowing-bot')
    if channel:
        await channel.send(messages[index])

    # Update the index for the next message
    next_index = (index + 1) % len(messages)
    update_message_index(next_index)

    # Close the bot after sending the message
    await client.close()

client.run(TOKEN)

