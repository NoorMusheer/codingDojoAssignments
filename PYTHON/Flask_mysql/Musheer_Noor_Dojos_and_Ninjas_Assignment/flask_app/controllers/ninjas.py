from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template, redirect, request, session
import time

@app.route('/add_ninja')
def add_ninja_page():
    all_dojos = Dojo.display_all_records()
    return render_template("add_new_ninja.html", all_dojos = all_dojos)

@app.route('/ninja_added', methods=['POST'])
def new_ninja_info():
        session['fname'] = request.form['fname']
        session['lname'] = request.form['lname']
        session['age'] = request.form ['age']
        data = {
            "dojo_id" : request.form['dojo_id'],
            "first_name" : request.form['fname'],
            "last_name" : request.form['lname'],
            "age" : request.form['age']
        }
        Ninja.create_ninja(data)
        return redirect("/ninja_page")

@app.route('/ninja_page')
def show_new_ninja():
    return render_template("confirm_ninja.html")

@app.route('/edit_ninja/<int:id>')
def edit_ninja(id):
    nnja_info = Ninja.get_ninja_by_id(id)
    return render_template("edit_ninjas.html", nnja_info = nnja_info)

@app.route('/edit_ninja')
def new_ninja_correction():
    return redirect("edit_ninjas.html")

@app.route('/delete_ninja/<int:NinId>/<int:id>')
def delete_ninja(NinId, id):
    Ninja.delete_ninja(NinId)
    return redirect("/dojos/" + str(id))

@app.route('/ninja_update', methods=['POST'])
def updated_ninja():
    data = {
        "id":request.form['id'],
        "first_name" : request.form['fname'],
        "last_name" : request.form['lname'],
        "age": request.form['age']
    }
    Ninja.update_ninja(data)
    return redirect('/confirm_update')

@app.route('/confirm_update')
def confirm_update():
    return render_template('/updated_ninja.html')