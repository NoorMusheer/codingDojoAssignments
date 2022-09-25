from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)


@app.route('/users', methods=['POST'])
def create_user():
    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "email" : request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/users/new')
def form_file():
    return render_template("new.html")







if __name__ == "__main__":
    app.run(debug=True)    