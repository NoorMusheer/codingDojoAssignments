from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/withjinja2/<string:anything>/<int:num>')
def with_jinja2(anything, num):
    return render_template ("anything.html", anything=anything, num=num)

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