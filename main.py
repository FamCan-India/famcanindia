# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/acknowledgements")
def acknowledgements():
    return render_template("acknowledgements.html")

@app.route("/affiliations")
def affiliations():
    return render_template("affiliations.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/data-overview")
def data_overview():
    return render_template("data_overview.html")

@app.route("/stats-overview")
def stats_overview():
    return render_template("stats_overview.html")

if __name__ == "__main__":
    app.run(debug=True)
