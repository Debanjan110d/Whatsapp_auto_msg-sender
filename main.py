# This program sends a WhatsApp message to a specific number at the specified time.
# It uses the pywhatkit library which is a Python wrapper for WhatsApp Web.
# The program takes the phone number, message, hour and minute as input and sends the message at the specified time.

import pywhatkit as kit
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import time

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
        # Make sure the phone number is in the correct format
        phone_number = phone_number.replace(" ", "").replace("-", "")
        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number

        # Check if the time has already passed
        now = datetime.now()
        if hour < now.hour or (hour == now.hour and minute <= now.minute):
            return False, "Please select a future time"

        # Add a small delay to ensure WhatsApp Web is ready
        kit.sendwhatmsg(phone_number, message, hour, minute, wait_time=15)
        return True, "Message scheduled successfully! Please keep WhatsApp Web open."
    except Exception as e:
        if "web.whatsapp.com" in str(e):
            return False, "Please make sure WhatsApp Web is logged in and try again"
        return False, f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule_message():
    try:
        data = request.get_json()
        phone = data.get('phone')
        message = data.get('message')
        datetime_str = data.get('datetime')
        
        # Convert datetime string to hour and minute
        dt = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        hour = dt.hour
        minute = dt.minute
        
        # Clean phone number
        phone = ''.join(filter(lambda x: x.isdigit() or x == '+', phone))
        
        success, msg = send_whatsapp_message(phone, message, hour, minute)
        
        return jsonify({
            'success': success,
            'message': msg,
            'scheduledTime': {
                'hour': hour,
                'minute': minute
            }
        })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': "Error scheduling message. Please make sure WhatsApp Web is open and try again."
        })

if __name__ == "__main__":
    app.run(debug=True)

