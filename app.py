from flask import Flask
import threading
import main # Yahan 'import main' likhein

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def start_bot():
    # main.py mein aapne 'app' variable banaya hai, isliye main.app.run()
    main.app.run() 

if __name__ == '__main__':
    threading.Thread(target=start_bot).start()
    app.run(host='0.0.0.0', port=10000)
    
