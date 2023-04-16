from flask import Flask
from threading import Thread
from csv_processor import load_csv

app = Flask('My First Server')

@app.route('/')
def home():
    return "The server is running"

def run():
    """
    This method runs the server on port 8080
    """
    app.run(host='127.0.0.1', port=8080)

def keep_alive():
    """
    This method starts the server on its own thread
    """
    t = Thread(target=run)
    t.start()