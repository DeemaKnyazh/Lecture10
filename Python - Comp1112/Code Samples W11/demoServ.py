from flask import Flask
from threading import Thread

app = Flask('My First Server')

@app.route('/') # Decorator that specifies the URL for this method, in this case its just http://0.0.0.0/
def home():
    return "The server is running"