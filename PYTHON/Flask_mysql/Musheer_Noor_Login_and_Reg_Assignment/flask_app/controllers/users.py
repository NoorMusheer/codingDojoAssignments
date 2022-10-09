from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/') 
def index():
    session.clear()
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    return render_template("/welcome.html")

@app.route('/register', methods=['POST'])
def register_user():
    user_data={
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "dob" : request.form['dob'],
        "favorite_language" : request.form['favorite_language'],
        "password" : request.form['password'],
        "password2" : request.form['password2']
            }
    user = User.get_user_by_email(user_data)
    if not User.validate_reg(user_data, user):
        return redirect('/welcome')
    User.create_user(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['dob'] = request.form['dob']
    session['favorite_language'] = request.form['favorite_language']
    return redirect('/confirm_reg')

@app.route('/confirm_reg')
def confirm_registration():
    return render_template("confirm_reg.html")

@app.route('/login')
def login_user():
    return render_template("login.html")

@app.route('/check_login', methods = ["POST"])
def validate_login():
    login_data={
        "email" : request.form['email'],
        "password": request.form['password']
    }
    user = User.get_user_by_email(login_data)
    if not User.validate_login(login_data,user):
        return redirect('/login')
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not session:
        return redirect('/')
    return render_template('dashboard.html')