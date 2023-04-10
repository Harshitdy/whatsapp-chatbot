from flask import Flask, request
from twilio.rest import Client
import os
from marketstack import get_stock_price


app = Flask(__name__)


account_sid = os.getenv('TWILIO_ACCOUNT')
auth_token = os.getenv('TWILIO_TOKEN')

client = Client(account_sid, auth_token)
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

def process_message(msg):
    if msg.lower() == 'hi':
        response = "Hello, Welcome to Harshit's stock market bot! Please write your preffered stock in short form (symbol). i.e. 'Apple' -> 'AAPL' "
    else:
        response = get_stock_price(msg.upper())
    return response

def send_message(msg, recipient):
    client.messages.create(
    from_= TWILIO_NUMBER,
    body=msg,
    to= recipient   
    )


@app.route('/')
def home():
    return {"Results":"Hello World!"}


@app.route('/webhook', methods=['POST'])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_message(msg)
    send_message(response, sender)
    return "Ok", 200