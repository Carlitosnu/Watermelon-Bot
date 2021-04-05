# 🔶 On develoment
from discord.ext import commands
from discord import Embed

# FFmpegPCMAudio, PCMVolumeTransformer
# from discord.utils import get
# import youtube_dl
# import os
# from utils.getClient import GetClient

# client = GetClient().voice_clients


class VoiceChannel_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="entrar",
        usage="enter [url]",
        description="Consulta el clima de tu ciudad y te lo regresa",
        pass_context=True,
    )
    async def enter(self, ctx):
        if ctx.voice_client:
            embed = Embed(
                title="❌ Ya estoy en un canal",
                description="Desconectame y vuelveme a conectar",
            )
            await ctx.send(embed=embed)
        elif ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send("✅ Estoy dentro!")
        else:
            embed = Embed(
                title="❌ No has entrado a ningún canal",
                description="Entra a un canal y vuelve a intentarlo",
            )
            await ctx.send(embed=embed)

    @commands.command(
        name="salir",
        usage="salir",
        description="Con este comando el bot sale del canal de voz",
    )
    async def leave(self, ctx):
        if ctx.voice_client:
            print(ctx.voice_client)
            await ctx.guild.voice_client.disconnect()
            await ctx.send("✅ Sali del canal")
        else:
            embed = Embed(
                title="❌ No estoy en un canal",
                description="Primero debo estar en uno para salir",
            )
            await ctx.send(embed=embed)

    # # Lo dificil :S
    # @commands.command(
    #     name="play",
    #     usage="play [url]",
    # )
    # async def play(self, ctx, url: str):
    #     # Esto elimina la cancion anterior para cambiarla
    #     channel = ctx.voice_client
    #     if not channel:
    #         embed = Embed(
    #             title=":x: No estoy en un canal de voz",
    #             description="Para eso deberas ejecutar el comando **w!entrar** "
    #         )
    #         await ctx.send(embed=embed)
    #         return
    #     song = os.path.isfile("song.mp3")
    #     try:
    #         if song:
    #             os.remove("song.mp3")
    #     except PermissionError:
    #         print("No se puede eliminar la canción por que se esta escuchando")
    #         await ctx.send(":x: No se puede eliminar la canción por que se esta escuchando")
    #         return
    #     voice = get(channel, guild=ctx.guild)

    #     ylOps = {
    #         "format": "bestaudio/best",
    #         "postprocessors": [{
    #             'key': "FFmpegExtractAudio",
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192'
    #         }]
    #     }

    #     with youtube_dl.YoutubeDL(ylOps) as yld:
    #         print(f"Downloading {url}")
    #         yld.download([url])

    #     for file in os.listdir("./"):
    #         if file.endswith(".mp3"):
    #             name = file
    #             print(f"Archivo {file} renombrado")
    #             os.rename(file, "song.mp3")

    #     voice.play(FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"La canción {name} termino."))
    #     voice.source = PCMVolumeTransformer(voice.source)
    #     voice.source.volume = 0.07

    #     nname = name.rsplit("-", 2)
    #     await ctx.send(f"✅ Reproduciendo {nname}")


def setup(bot):
    bot.add_cog(VoiceChannel_Commands(bot))
