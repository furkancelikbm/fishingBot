import requests

# Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = '7709512017:AAEsEEPDq-DqqXSIiaEoZhV5wOAkIyUpi4g'
CHAT_ID = '1072767279'


def get_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    return response.json()


def send_telegram_message(message): 
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'  # Optional: you can use HTML too
    }
    response = requests.post(url, json=payload)
    response_data = response.json()
    if 'result' in response_data:
        print("Message sent successfully:", response_data)
    else:
        print("Failed to send message:", response_data)

        
def send_telegram_photo(photo_path, caption=""):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        payload = {
            'chat_id': CHAT_ID,
            'caption': caption,
        }
        response = requests.post(url, data=payload, files={'photo': photo})
        response_data = response.json()
        if 'result' in response_data:
            print("Photo sent successfully:", response_data)
        else:
            print("Failed to send photo:", response_data)

