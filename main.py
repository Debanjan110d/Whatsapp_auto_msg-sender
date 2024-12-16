# This program sends a WhatsApp message to a specific number at the specified time.
# It uses the pywhatkit library which is a Python wrapper for WhatsApp Web.
# The program takes the phone number, message, hour and minute as input and sends the message at the specified time.

import pywhatkit as kit

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
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Your details
    phone_number = ""  #  number with country code
    message = """ Hello! This is a test message."""
    
    # Time to send the message (3rd December at 00:13)
    # 0-23 for hour and 0-59 for minute
    hour = 0  
    minute = 13
    
    # Send the message
    send_whatsapp_message(phone_number, message, hour, minute)

