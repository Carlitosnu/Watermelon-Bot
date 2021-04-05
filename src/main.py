from discord.ext import commands
from utils.getEnv import getEnv, load_env

# from keep_alive import keep_alive

# Load enviroments from .env file
load_env()

# Create bot client
prefix = getEnv("BOT_PREFIX")
description = getEnv("BOT_DESCRIPTION")
client = commands.Bot(command_prefix=prefix, description=description)


# On bot ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# Load the extensions or cogs
cogs = ["cogs.ping", "cogs.joke", "cogs.clima", "cogs.canalVoz"]
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as err:
        print(f"An error has occurred {err}")

# keep_alive()

# Run the bot
if __name__ == "__main__":
    client.run(getEnv("BOT_TOKEN"))
