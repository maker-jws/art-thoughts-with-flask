from api.data import data
from api.source import source
import os
from flask import Flask, g, session
from flask_login import LoginManager
from flask_cors import CORS
import models

DEBUG = True
PORT = 8000

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')  # decorator will invoke Flask
def index():  # creates
    message = 'hello human = 01001000 01101001 00100000 01001000 01110101 01101101 01100001 01101110 0001010'
    return message


CORS(data, origins=["http://localhost:3000"], supports_credentials=True)
CORS(source, origins=["http://localhost:3000"], supports_credentials=True)
app.register_blueprint(data)
app.register_blueprint(source)

if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
