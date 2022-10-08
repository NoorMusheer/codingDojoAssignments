from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.friendship import Friendship
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/friendships')


@app.route('/friendships')
def friendships():
    all_friendships = Friendship.get_all_friendships()
    all_users = User.get_all_users()
    return render_template("index.html", all_friends = all_friendships, all_users = all_users)

@app.route('/create_friends', methods=['POST'])
def create_friends():
    data={
        "id1": request.form['user_id'],
        "id2": request.form['user2_id']
    }
    Friendship.add_friendship(data)
    return redirect('/friendships')