from flask import Flask, render_template, request, jsonify
import discord
from discord.ext import commands
import asyncio

app = Flask(__name__)

# Discord бот
TOKEN = "MTMwNzI1MDAyNTExMzQ1NjY2MQ.GeZa1l.aTYvqq4i8e1VYmZY5C3b2ypcZSDnaZ3n4TIQO8"
GUILD_ID = "662267976984297473"
CHANNEL_ID = "1307251332381413467"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Асинхронный клиент
client_loop = asyncio.get_event_loop()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "Введите запрос"}), 400

    async def send_prompt():
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(f"/imagine prompt: {prompt}")

    client_loop.create_task(send_prompt())
    return jsonify({"message": "Запрос отправлен!"})


# Запуск Discord бота в отдельной задаче
def run_discord_bot():
    @bot.event
    async def on_ready():
        print(f"{bot.user} подключен к Discord!")

    client_loop.create_task(bot.start(TOKEN))


if __name__ == "__main__":
    # Запуск Discord клиента
    client_loop.create_task(asyncio.to_thread(run_discord_bot))
    # Запуск Flask
    app.run(debug=True)
