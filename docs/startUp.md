# Ejecutar
## Antes de empezar
Antes de ejecutar tu codigo requeriras renombrar el archivo ```.env.example``` y dejarlo asi ```.env``` y en ese archivo remplazaras la información por la que obtubiste
   ```
   BOT_TOKEN = El token de tu bot
   BOT_PREFIX = Como quieres que llamen a tu bot
   BOT_DESCRIPTION = Describe que hara
   OPEN_WEATHER_KEY = El api de Open Weather Map
   ```

## Ejecución
Abrimos una terminal en la carpeta del proyecto y ejecutamos:
   ```shell
   #Iniciamos un entorno protegido
   pipenv shell

   #Instalamos las dependecias
   pipenv install

   #Instalamos dependecias de desarrollo.
   pipenv install --dev

   #Iniciamos el bot
   pipenv run start
   ```

Siguiente paso: [Subir codigo](docs/upload.md)

**© Watermelon Code**