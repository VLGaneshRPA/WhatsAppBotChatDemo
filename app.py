from flask import Flask
from flask import request
import twilio
from twilio.rest import Client
import os
from marketShare import getStockPrice

#initialize falsh application name
app =  Flask(__name__)

#retrieve Twilio 
ACCOUNT_ID  = os.environ.get('TWILIO_ACC_SID')
ACCOUNT_TOKEN  = os.environ.get('TWILIO_ACC_TOEKN')
client = Client(ACCOUNT_ID,ACCOUNT_TOKEN)

#TWILIO SANDBOX Number
TWILIO_NUMBER = 'whatsapp:+14155238886'

@app.route('/')
def home():
    return {
        "Result": "Successfully created the first route, cheers!"
        }

def process_msg(msg):
    response = ''
    i = 0
    if msg.lower() == 'hi':
        i+=1
        response = 'Hello, Welcome to First Chat Bot to get the Stock Price! '
        response += 'Please enter a valid stock code in the following format i.e., sym: <stock_symbol> to get the price details'
    elif 'sym:' in msg:
        data = msg.split(':')
        stock_code = data[1].strip()
        last_price = getStockPrice(stock_Symbol=stock_code)
        response = f'Last price of the stock {stock_code} is: {last_price}'
    elif i > 1:
        response = 'Please enter a valid code in valid format i.e., sym: AAPL'
    else:
        response = 'Please type hi to start the conversation'
    return response

def send_msg(msg,recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient)

@app.route('/webold', methods=['POST'])
def webhookold():
    message = request.form['message']
    return {
        "Result": f'message is {message}'
        }
    
@app.route('/webhook', methods=['POST'])
def webhook():
    #for debugging
    #import pdb
    #pdb.set_trace()
    f = request.form
    #msg = f['Body']
    #either format working
    msg = f.get('Body')
    sender = f['From']
    response = process_msg(msg=msg)
    print(f'msg: {response} sender {sender}')
    send_msg(msg=response,recipient=sender)
    return 'OK', 200
        
#Steps to reponse to Whatsapp msg using Twilio rest
# Get Twilio ACCOUNT_ID(SID), ACCOUNT_TOKEN and set as env variable
# Retrieve SID & TOKEN into the code
# import Twilio client
# initialize client
# method to process message
# method to respond message
# check in Whatsapp       
        
        
        
        