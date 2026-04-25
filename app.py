from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vendors")
def vendors():
    return render_template("vendors.html")


@app.route("/produce")
def produce():
    return render_template("produce.html")


if __name__ == "__main__":
    app.run(debug=True)
