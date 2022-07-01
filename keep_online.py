from flask import Flask
from threading import Thread

name = None

app = Flask(__name__)

@app.route('/')
def home():
    global name
    return f"Online as {name}"

def run():
    app.run(host='0.0.0.0',port=8080)

def start(user):
    global name
    name = user
    t = Thread(target=run)
    t.start()