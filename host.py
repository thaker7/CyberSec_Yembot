from flask import Flask, request
from threading import Thread

app = Flask('')

@app.route('/https://cybersec-yembot.onrender.com')
def home():
    return "<b> hello</b>"

def run():
    app.run()

def keep_alive():
    t = Thread(target=run)
    t.start()
