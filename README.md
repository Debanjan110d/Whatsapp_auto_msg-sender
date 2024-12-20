# WhatsApp Message Sender Using Pywhatkit

This Python program allows you to schedule and send WhatsApp messages at a specific time using the **Pywhatkit** library, which automates WhatsApp Web. It's easy to use and requires minimal setup.

## Features

-  Schedule WhatsApp messages to any phone number with a valid country code.
-  Simple and user-friendly Python script.
-  Uses the `pywhatkit` library for automation.

## Prerequisites

Before running this program, ensure the following:

1. **Python** is installed on your system (Python 3.7 or higher recommended).
2. Install the required `pywhatkit` library.
3. WhatsApp Web must be set up on your default web browser.

## Installation Steps

Follow these steps to get the program up and running:

### Step 1: Install Python

Download and install Python from the [official Python website](https://www.python.org/downloads/). Ensure you check the box to **add Python to PATH** during installation.

### Step 2: Install pywhatkit

Open your terminal (or command prompt) and run the following command:

```bash
pip install pywhatkit
```

### Step 3: Create the Python Script

Save the following code in a file named `send_whatsapp_message.py`:

```python
import pywhatkit as kit

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message, hour, minute):
    """
    Sends a WhatsApp message to a specific number at the specified time.

    Args:
    phone_number (str): The recipient's phone number (e.g., '+91xxxxxxxxxx').
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
    # Input your details here
    phone_number = "+91XXXXXXXXXX"  # Replace with the recipient's number
    message = "Hello! This is a test message."

    # Specify the time (24-hour format)
    hour = 0  # Hour (0-23)
    minute = 13  # Minute (0-59)

    # Send the message
    send_whatsapp_message(phone_number, message, hour, minute)
```

### Step 4: Run the Program

1. Open your terminal or command prompt.
2. Navigate to the folder containing the script.
3. Run the script using the following command:

```bash
python send_whatsapp_message.py
```

### Step 5: Follow the Prompts

-  Make sure your **WhatsApp Web** is already logged in.
-  At the scheduled time, the browser will open automatically and send the message.

## Notes

-  The phone number must include the **country code** (e.g., `+91` for India).
-  The message scheduling time should be at least **2 minutes ahead** of your current time to avoid errors.
-  Ensure a stable internet connection for the script to function properly.

## Example

For a message to be sent at **12:13 AM** to the phone number `+911234567890`:

```python
phone_number = "+911234567890"
message = "Hello! This is an automated message."
hour = 0  # Midnight
minute = 13
```

## Author

**Debanjan**

Feel free to use, modify, and share this script for your personal projects!

---

### Troubleshooting

If you encounter errors:

-  Verify your internet connection.
-  Ensure you are logged into **WhatsApp Web** in your browser.
-  Update the `pywhatkit` library if necessary:

```bash
pip install --upgrade pywhatkit
```
