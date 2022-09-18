from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_app():
    return "Hello World! "


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def say(name):
    return f"Hi {name}! "


@app.route('/repeat/<int:times>/<words>')
def repeat(times, words):
    return f"{times * words}"

@app.errorhandler(404)
def invalid_route(e):
    return "Sorry! No Response. Try Again. "

if __name__ == "__main__":
    app.run(debug=True)
