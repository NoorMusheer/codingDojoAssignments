from flask_app import app
from flask_app.models.ninja import Ninja
from flask import render_template, redirect, request

@app.route('/add_ninja')
def add_ninja_page():
    return render_template("add_new_ninja.html")

