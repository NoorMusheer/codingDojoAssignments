from os import times
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_app():
    return "Hello World! "


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<str:name>')
def say(name):
    return f"Hi {name}! "


@app.route('/repeat/<int:times>/<str:words>')
def repeat(times, words):
    return f"{times * words}"



if __name__ == "__main__":
    app.run(debug=True)
