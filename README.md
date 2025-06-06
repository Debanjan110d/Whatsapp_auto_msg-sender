# WhatsApp Auto Message Scheduler

A web-based application that allows you to schedule WhatsApp messages to be sent at specific times. Built with Python Flask and the PyWhatKit library. This application provides a user-friendly web interface for scheduling WhatsApp messages without needing to write any code.

## Features

- 🕒 Schedule messages for future delivery
- 📱 Web interface for easy message scheduling
- ⏰ Real-time countdown timer
- 📊 Clear status updates and error handling
- 🔒 Works with WhatsApp Web (secure and no API keys needed)
- 🎯 Intuitive user interface
- 📱 Responsive design for mobile and desktop
- ⚡ Real-time validation and error checking

## Prerequisites

Before running this application, ensure you have:

1. **Python** installed (3.7 or higher recommended)
2. A modern web browser (Chrome recommended)
3. Active internet connection
4. WhatsApp account and access to WhatsApp Web

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Whatsapp_auto_msg-sender.git
cd Whatsapp_auto_msg-sender
```

2. Install required packages:
```bash
pip install flask pywhatkit
```

## Usage

1. Start the application:
```bash
python main.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Before scheduling messages:
   - Open WhatsApp Web in another browser tab
   - Scan the QR code to log in
   - Keep WhatsApp Web open while using the scheduler

4. To schedule a message:
   - Enter the recipient's phone number with country code (e.g., +91XXXXXXXXXX)
   - Type your message
   - Select the date and time for delivery
   - Click "Schedule Message"
   - Wait for the confirmation message

## Important Notes

- Keep your computer awake and connected to the internet
- Don't close WhatsApp Web or the scheduler page
- Schedule messages at least 1 minute in the future
- Make sure to include the country code in phone numbers
- The application uses Flask's development server, suitable for personal use

## Technical Details

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- WhatsApp Integration: PyWhatKit library
- Real-time updates using JavaScript intervals
- Responsive design for mobile and desktop

## Project Structure

```
Whatsapp_auto_msg-sender/
├── main.py              # Flask application and message scheduling logic
├── static/
│   └── style.css       # CSS styling for the web interface
├── templates/
│   └── index.html      # HTML template for the web interface
└── README.md           # Project documentation
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid phone numbers
- Past date/time selection
- WhatsApp Web connection issues
- Network connectivity problems

## Author

**Debanjan Dutta**

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- PyWhatKit library for WhatsApp integration
- Flask framework for the web interface
- The open-source community for inspiration and support

## Disclaimer

This project is for educational purposes only. Please ensure you comply with WhatsApp's terms of service and policies when using this application.
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
