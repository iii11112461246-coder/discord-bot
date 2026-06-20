import discord
from discord.ext import commands

TOKEN = "MTUxNzg5MDk0MzI4NDQxNjU3Mg.GQ_ZwG.xVfUirtasr1cTevMAjVS2arko3jMOvISRDNHQI"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 로그인 성공!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "안녕" in message.content:
        await message.channel.send("안녕하세요!")

    await bot.process_commands(message)

bot.run(TOKEN)
