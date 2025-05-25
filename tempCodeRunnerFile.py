# This program sends a WhatsApp message to a specific number at the specified time.
# It uses the pywhatkit library which is a Python wrapper for WhatsApp Web.
# The program takes the phone number, message, hour and minute as input and sends the message at the specified time.

import pywhatkit as kit
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message, hour, minute):
    """
    Sends a WhatsApp message to a specific number at the specified time.
    
    Args:
    phone_number (str): The recipient's phone number (with country code, e.g., '+91xxxxxxxxxx').
    message (str): The message to send.
    hour (int): Hour in 24-hour format (e.g., 0 for midnight).
    minute (int): Minute of the hour.
    """
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        return True, "Message scheduled successfully!"
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule_message():
    try:
        phone = request.form.get('phone')
        message = request.form.get('message')
        datetime_str = request.form.get('datetime')
        
        # Convert datetime string to hour and minute
        dt = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        hour = dt.hour
