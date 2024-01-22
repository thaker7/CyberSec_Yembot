from info import *
from flask import Flask, request
from threading import Thread
import telebot

TOKEN = TOKEN_BOT
WEBHOOK_URL = "https://cybersec-yembot.onrender.com/"
app = Flask('')

@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

def run():
    app.run()

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == '__main__':
    bot.remove_webhook()     # حذف الويبهوك
    bot.set_webhook(url=WEBHOOK_URL)  # تعيين الويبهوك
    keep_alive()
    