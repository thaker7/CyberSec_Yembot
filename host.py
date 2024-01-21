from flask import Flask, request
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<b> hell Cyber Security</b>"

def run():
    app.run(host='0.0.0.0', port=3001)

def keep_alive():
    t = Thread(target=run)
    t.start()
