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

# help
@client.command()
async def help(ctx):
    Des = """
    Hecho por El Equipo de WatermelonCode
    """
    embed = discord.Embed(
      title = 'Comandos generales',
      description = Des,
      color = discord.Color.random(),
      footer=ctx.message.created_at
      
      )
    embed.add_field(name="Comando w!ping", value="Devuelve: pong" , inline=True)
    embed.add_field(name="Comando w!clima pais", value="Devuelve la temperatura, Humedad y viento del pais dado, ejemplo: w!clima ecuador", inline=True)
    embed.add_field(name="Comando w!joke", value="Devuelve un chiste" , inline=True)
    embed.add_field(name="Creadores activos", value="Teo, CarlosThePro, Alexander, Jesus Crespo" , inline=True)
    await ctx.send(embed = embed)



# Load the extensions or cogs
cogs = ["cogs.ping", "cogs.joke", "cogs.clima", "cogs.moderation", "cogs.avatar"]
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as err:
        print(f"An error has occurred {err}")

# keep_alive()

# Run the bot
if __name__ == "__main__":
    client.run(getEnv("BOT_TOKEN"))
