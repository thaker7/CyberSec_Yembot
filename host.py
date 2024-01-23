from flask import Flask, request
from info import *

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    webhook_data = request.json
    
    print(f"Received webhook payload: {webhook_data}")
    
    return "", 200
