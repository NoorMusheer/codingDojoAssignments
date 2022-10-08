from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.friendship import Friendship
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/add_user', methods = ['POST'])
def add_user():
    user_data={
        "first_name" : request.form['first_name'],
        "last_name": request.form['last_name']
    }
    User.add_user(user_data)
    return redirect("/") 

