import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_signal(signal_type, symbol, price, confidence, indicators_ready=None, prediction_window=None):
    message = (f"🚨 {signal_type.upper()} SIGNAL – {symbol}\n"
               f"▶️ Price: {price}\n"
               f"🤖 Confidence: {confidence}%\n"
               f"📊 Indicators Ready: {indicators_ready}\n"
               f"⏰ Prediction Window: {prediction_window} candles")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'HTML'}
    requests.post(url, json=payload)
