import os
from flask import Flask, request
import telebot

TOKEN = os.getenv("BOT_TOKEN")  # Токен з Render environment variables
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Вас приветствует Аноним Бот 🤖")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://anon-bot-5ma6.onrender.com/{TOKEN}")
    return "Бот запущен!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
