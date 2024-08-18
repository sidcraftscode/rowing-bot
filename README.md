# Rowing Bot
A discord bot built for the [r/Rowing discord community](https://discord.gg/Mujt9ATJjp) that automatically sends the workout of the week in the `#workout-of-the-week` channel from a list of 52 workouts. It uses Python 3 and [discord.py](https://github.com/Rapptz/discord.py). It runs on **GitHub actions** weekly using a cron job.

## Running the project locally
### Prerequisites
python3

### Installation
1. Install dependencies
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2. Create a .env file and add the discord token for your bot to it
In the shell run:
```
touch .env
```

To `.env` add:
```
export DISCORD_BOT_TOKEN="your token here"
```

Then run in the shell
```
source .env
```

3. Open `bot.py` and change the name of the channel to the channel you want to send the messages to
```
channel_name = 'workout-of-the-week'
```

4. Run the python file
```
python main.py
```

## Built with
* Python 3
* discord.py

## Features
- [x] Sends a workout each week to the workout-of-the-week channel
- [x] Runs automatically on GitHub actions

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
