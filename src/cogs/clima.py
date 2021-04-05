# ✅ PASS

from discord.ext import commands
from utils.fetch import get
from utils.getEnv import getEnv
import discord


class Clima_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="clima",
        usage="*clima [ciudad]",
        description="Consulta el clima de tu ciudad y te lo regresa",
    )
    async def clima(self, ctx, city):
        api = getEnv("OPEN_WEATHER_KEY")
        print(city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
        r = get(url)
        print(r[0])
        if r[0] == 200:
            city_name = r[1]["name"]
            c = r[1]["main"]["temp"] - 273.15
            c = round(c)
            veloc = r[1]["wind"]["speed"]
            humedad = r[1]["main"]["humidity"]
            embed = discord.Embed(
                title=f"Temperatura en {city_name}",
            )
            embed.add_field(
                name=":white_sun_small_cloud: Temperatura",
                inline=False,
                value=f"{c}°",
            )
            embed.add_field(name=":droplet: Humedad", inline=True, value=f"{humedad}%")
            embed.add_field(name=":cloud: Viento: ", inline=True, value=f"{veloc} m/s")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f":x: Error **{r[0]}**")


def setup(bot):
    bot.add_cog(Clima_Command(bot))
