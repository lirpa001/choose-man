import discord
from discord.ext import commands
import random
from flask import Flask
import threading
import os

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def choose(ctx, *, choices: str):
    options = choices.split()
    if options:
        await ctx.send(f"🎲 我選擇：**{random.choice(options)}**")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    # 讀取 Render 後台設定的環境變數
    bot.run(os.environ.get('DISCORD_TOKEN'))