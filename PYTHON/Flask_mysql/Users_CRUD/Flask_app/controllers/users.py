from Flask_app import app
from flask import render_template, redirect, request
from Flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
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

@app.route('/users/delete/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/')

@app.route('/users/show/<int:id>')
def show_user(id):
    user = User.get_user_by_id(id)
    return render_template('/show.html', user = user)

@app.route('/users/edit/<int:id>')
def pre_fill_edit_page(id):
    user = User.get_user_by_id(id)
    return render_template("update.html", user = user)

@app.route('/users/update_data', methods=['POST'])
def update_user_data():
    data = {
        "id": request.form['id'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    User.update(data)
    return redirect('/')