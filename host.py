from info import *
from flask import Flask, request
from threading import Thread
import telebot

app = Flask(__name__)

# عملية الربط مع الويبهوك
@app.route('/6758499492:AAG-E9c1uDgXwAMgXGVH-aWpUDjfYG-spvw', methods=['POST'])
def respond():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK"

# تعيين عنوان الويبهوك
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://cybersec-yembot.onrender.com/6758499492:AAG-E9c1uDgXwAMgXGVH-aWpUDjfYG-spvw")  # استبدل هذا بعنوان الويبهوك الخاص بك

if __name__ == "__main__":
    set_webhook()  # تعيين الويبهوك عند تشغيل التطبيق
    app.run()
    