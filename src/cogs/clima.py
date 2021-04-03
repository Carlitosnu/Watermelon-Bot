# WARNING IN DEVELOMENT [95%]
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
        c = r[1]["main"]["temp"] - 273.15
        city_name = r[1]["name"]
        if r[0] == 200:
            embed = discord.Embed(
                title=f"Temperatura en {city_name}",
                description=f":white_sun_small_cloud: {c}°",
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f":x: Error **{r[0]}**")


def setup(bot):
    bot.add_cog(Clima_Command(bot))
