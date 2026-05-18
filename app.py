from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vendors")
def vendors():
    return render_template("vendors.html", list_of_vendors=["Vendor 1", "Vendor 2"])


@app.route("/produce")
def produce():
    return render_template("produce.html", list_of_produce=["Produce 1", "Produce 2"])


if __name__ == "__main__":
    app.run(debug=True)
