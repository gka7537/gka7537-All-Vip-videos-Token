from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

# Render port 10000 par expect karta hai
PORT = 10000 

@app.route('/')
def home():
    return "Bot is running on port 10000!"

def run_web():
    # Yahan port 10000 force kiya gaya hai
    app.run(host='0.0.0.0', port=PORT)

if __name__ == '__main__':
    t = Thread(target=run_web)
    t.start()
    
    # Yahan se aapka main bot run hoga
    import bot 
