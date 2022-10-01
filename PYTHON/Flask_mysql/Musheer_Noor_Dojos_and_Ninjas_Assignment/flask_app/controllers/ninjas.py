from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template, redirect, request, session

@app.route('/add_ninja')
def add_ninja_page():
    all_dojos = Dojo.display_all_records()
    return render_template("add_new_ninja.html", all_dojos = all_dojos)

@app.route('/ninja_added', methods=['POST'])
def new_ninja_info():
    data = {
        "dojo_id" : request.form['dojo_id'],
        "first_name" : request.form['fname'],
        "last_name" : request.form['lname'],
        "age" : request.form['age']
    }
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['age'] = request.form ['age']
    Ninja.create_ninja(data)
    return redirect("/ninja_page")

@app.route('/ninja_page')
def show_new_ninja():
    return render_template("confirm_ninja.html")

@app.route('/edit_ninja')
def edit_ninja():
    return render_template("edit_ninjas.html")

@app.route('/delete_ninja/<int:id>')
def delete_ninja():
    return render_template("dojo_info.html")