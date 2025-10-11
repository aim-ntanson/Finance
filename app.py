from flask import Flask
import telepot
from telebot.credentials import bot_token, URL, SECRET_NUM
from telebot.add import add

global bot
global TOKEN
TOKEN = bot_token
bot = telepot.Bot(TOKEN)
bot.setWebhook(URL.format(SECRET_NUM), max_connections=1)

app = Flask(__name__)

"""
Define a function to handle the message from telegram
for example:
    - /start: send a welcome message
    - /add {amount} {note}: add a new row to google sheets
"""


@app.route('/{}'.format(SECRET_NUM), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]
            # bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
            if text == "/start":
                welcome_message = "Welcome to my bot!"
                bot.sendMessage(chat_id, welcome_message)
            elif text.startswith("/add"):
                add(bot, text, chat_id)
            else:
                bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
        else:
            bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
    return "OK"


@app.route('/get_me', methods=['GET', 'POST'])
def get_me():
    return bot.getMe()


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Service is running!'


if __name__ == '__main__':
    app.run(threaded=True)
