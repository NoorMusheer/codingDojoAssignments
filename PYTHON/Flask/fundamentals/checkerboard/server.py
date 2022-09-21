
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def board_1():
    return render_template ("checkerboard1.html")

@app.route('/<int:num_col>')
def board_2(num_col):
    return render_template ("checkerboard2.html", num_col=num_col)


@app.route('/<int:num_col>/<int:num_row>')
def board_3(num_col, num_row):
    return render_template ("checkerboard3.html", num_col = num_col, num_row = num_row)



if __name__=="__main__":
    app.run(debug=True)
