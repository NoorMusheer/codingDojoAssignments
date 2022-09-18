from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/success')
def success():
    return "This was Successful!"

@app.route('/hello/<name>')
def user(name):
    return f"Hello {name}. How are you?"
    

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id







if __name__ == "__main__":
    app.run(debug=True)