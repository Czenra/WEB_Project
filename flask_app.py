from flask import Flask, render_template, request
import solve
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_super_wordle_key'

#data_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data'), 'words.txt')
with open('data/words.txt', 'r') as f:
    word_list = f.read().splitlines()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/wordle_solver.html", methods=["GET", "POST"])
def wordle_solver():
    if request.method == "GET":
        return render_template("wordle_solver.html")

    if request.method == "POST":
        l_ex = request.form.get("letEX")
        l_pattern = [request.form.get("l1"), request.form.get("l2"), request.form.get("l3"), request.form.get("l4"),
                     request.form.get("l5")]
        y_pattern = [request.form.get("y1"), request.form.get("y2"), request.form.get("y3"), request.form.get("y4"),
                     request.form.get("y5")]
        return render_template("wordle_solver.html",
                               solution=solve.solve_wordle(word_list, l_ex, l_pattern, y_pattern))


@app.route("/known_words.html")
def known_words():
    return render_template("known_words.html")
