import datetime
import requests

"""
bot: bot object
text: text from telegram

1. This function will add a new row to google sheets
you should create sheetName on google sheets before using this function

2. Where the endures will type /add {amount} {long text note}
and the bot will add a new row to google sheets

3. For example: /add 1000 mua bim bim
"""
import re


def add(bot, text, chat_id):
    try:
        amount = int(re.search(r'/add\s+(\d+)', text).group(1)) * 1000
        name = re.search(r'/add\s+\d+\s+(.*)', text).group(1)
        date = datetime.datetime.now().strftime("%m/%d/%Y")
        sheetName = "{}/{}".format(datetime.datetime.now().month, datetime.datetime.now().year)
        action = "add"  # add
    except Exception as e:
        print(e)
        bot.sendMessage(chat_id, "Sorry, I didn't understand that kind of message")
        return

    # TODO you should change the url of your google script here
    url = ""
    data = {"name": name, "amount": amount, "date": date, "sheetName": sheetName}

    # Start request to google script then get response to send back to telegram
    r = requests.post(url, json=data)

    # sometime bot.sendMessage() doesn't work so we will ignore it
    try:
        bot.sendMessage(chat_id, "Response from google '{}'".format(r.text))
    except Exception as e:
        print(e)  # for DEBUG purpose
        print(r.text)  # for DEBUG purpose
    print(data)  # for DEBUG purpose
