import os, ollama, discord
from discord import Intents
from discord.ext import commands

MISTRAL_TOKEN = os.environ["MISTRAL_TOKEN"]

intents = Intents.all()
chat_log = []
client = commands.Bot(command_prefix="!", intents=intents, owner_id=1110526906106904626)


@client.event
async def on_ready() -> None:
    try:
        await client.change_presence(activity=discord.Streaming(name="message me", url="https://twitch.tv/gothamchess"))
        print(f"----- Mistral AI is Online -----\nServers: {len(client.guilds)}\nMembers: {len(client.users)}")

    except Exception:
        print(Exception)


@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    elif message.content.startswith("!"):
        pass
    else:
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.typing()
            num = 1
            while num != 0:
                chat_log.append({"role": "user", "content": message.content})

                chat_call = ollama.chat(model="mistral", messages=chat_log)
                response = chat_call["message"]["content"]
                chat_log.append({"role": "assistant", "content": response})

                await message.channel.send(response)
                num -= 1
                if num == 0:
                    break

    await client.process_commands(message)

client.run(MISTRAL_TOKEN)