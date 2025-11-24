import requests

BOT_TOKEN = "7825944734:AAFdOLdbktsjKZosUnT9gFZUnC2Ee3vZ1mA"
CHAT_ID = 8365201072  
TEXT = "Prueba desde send_message.py 😎"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    print("URL:", url)
    print("Payload:", payload)

    r = requests.post(url, json=payload)

    print("Status:", r.status_code)
    print("Raw body:", r.text)

    try:
        print("JSON:", r.json())
    except Exception as e:
        print("No JSON:", e)

if __name__ == "__main__":
    send_message(CHAT_ID, TEXT)
