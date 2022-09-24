from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Another random secret key."


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_data():
    print(request.form)
    session['username_first'] = request.form['first_name']
    session['username_last'] = request.form['last_name']
    session['user_location'] = request.form['user_location']
    session['user_fav_lang'] = request.form['user_fav_lang']
    session['user_comments'] = request.form['user_comments']
    print(session)
    return redirect('/result')

@app.route('/result')
def show_results():
    return render_template("result.html")






if __name__ == "__main__":
    app.run(debug=True)