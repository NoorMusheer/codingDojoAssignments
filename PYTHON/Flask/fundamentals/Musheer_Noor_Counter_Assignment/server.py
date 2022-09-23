from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "5C0mput3r8!*"


@app.route('/')
def keep_count():
    if "visits"  not in session: 
        session['visits'] = 0
    else:
        session['visits'] += 1
    print(request.form)
    return render_template("index.html")

@app.route('/2')
def add_by_two():
    session['visits'] += 1
    print(request.form)
    return redirect('/')

@app.route('/u', methods=['POST'])
def add_by_user_pick():
    user_num = request.form['user_add_by']
    session['visits'] += int(user_num)-1
    print(user_num)
    print(request.form)
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    print(request.form)
    return redirect('/')









if __name__=="__main__":
    app.run(debug=True)