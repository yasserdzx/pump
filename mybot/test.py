import requests

# Replace with your actual bot token and channel ID
BOT_TOKEN = '6481324501:AAE5oXRtA06_fpxM1npiPrNe_w5H-8MOfXo'
CHANNEL_ID = '@yassou_btc'  # Ensure this is correct

def send_message_to_channel(channel_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': channel_id,
        'text': message
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(f"Message sent to {channel_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e.response.content}")

# Test sending a message
send_message_to_channel(CHANNEL_ID, "Test message to the new channel")
