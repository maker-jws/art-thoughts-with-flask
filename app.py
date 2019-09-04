from flask import Flask
DEBUG = True
PORT = 8000

app = Flask(__name__)
@app.route('/')  # decorator will invoke Flask
def index():  # creates
    message = 'hello human = 01001000 01101001 00100000 01001000 01110101 01101101 01100001 01101110 0001010'
    return message


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
