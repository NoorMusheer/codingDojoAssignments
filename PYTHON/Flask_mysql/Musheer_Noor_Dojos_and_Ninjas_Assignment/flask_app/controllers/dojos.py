from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request


@app.route('/')
def index():
    return redirect ('/dojos')


@app.route('/dojos')
def dojo_records():
    all_dojos = Dojo.display_all_records()
    return render_template("dojos.html", all_dojos = all_dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo_page():
    data = {
        "name" : request.form['new_dojo']
    }
    Dojo.create_a_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:id>')
def show_dojo_ninjas(id):
    ninjas_list = Dojo.ninjas_by_dojo(id)
    print("-----HERE IS THE LIST RESULT -----")
    print(ninjas_list)
    return render_template("dojo_info.html", ninjas_list = ninjas_list)

