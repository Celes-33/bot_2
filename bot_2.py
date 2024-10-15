import discord
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$userinfo'):
        user_id = message.author.id
        user = await client.fetch_user(user_id)
        await message.channel.send(f"usuario:{user.name}, id:{user.id}")
    elif message.content.startswith('$sticker'):
        sticker_path = fetch_sticker()  # Obtén la ruta del sticker
        await message.channel.send(file=File(sticker_path))
    else:
        await message.channel.send("Lo siento, no entiendo ese comando")
 
client.run('MTI4ODMxNzYxNzc2MDg5NDk5Ng.GIbe6G.N8XqNXWG9pPTKTMO5zrGOi45mZdlsEUZTxlWhs')
