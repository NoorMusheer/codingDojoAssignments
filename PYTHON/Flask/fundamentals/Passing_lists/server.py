from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_lists():
    student_info=[
        {"name":"Adam", "age":20},
        {"name":"Brandy", "age":30},
        {"name":"Charles", "age":40},
        {"name":"Diana", "age":50},
    ]
    return render_template("index.html", student_info = student_info)






if __name__ == "__main__":
    app.run(debug=True)
