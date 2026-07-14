from flask import Flask
import threading
import bot  # Yahan aapki bot wali file ka naam hona chahiye

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def start_bot():
    bot.run() # Ye command aapke bot ko start karegi

if __name__ == '__main__':
    # Ek thread mein bot chalayein, dusre mein web server
    threading.Thread(target=start_bot).start()
    app.run(host='0.0.0.0', port=10000)
    
