from Flask_app import app
from flask import render_template, redirect, request, session
from Flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("users.html", all_users = users)


@app.route('/users', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/users/new')
    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "email" : request.form['email']
    }
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    User.save(data)
    return redirect('/users/show_recent')

@app.route('/users/new')
def form_file():
    return render_template("new.html")

@app.route('/users/delete/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/')

@app.route('/users/show_recent')
def display_just_added_info_test():
    return render_template('/show.html')


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