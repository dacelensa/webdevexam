from flask import Flask, render_template
import json
from datetime import datetime

with open("data/produce.json", "r", encoding="utf8") as f:
    all_produce = json.load(f)

with open("data/vendors.json", "r", encoding="utf8") as f:
    all_vendors = json.load(f)

app = Flask(__name__)


def get_season_name():
    current_month = datetime.now().month
    if current_month >= 3 and current_month <= 5:
        return "spring"
    if current_month >= 6 and current_month <= 8:
        return "summer"
    if current_month >= 9 and current_month <= 11:
        return "autumn"
    else:
        return "winter"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vendors")
def vendors():
    return render_template("vendors.html", list_of_vendors=["Vendor 1", "Vendor 2"])


@app.route("/produce")
def produce():
    in_season = []
    out_of_season = []
    current_season = get_season_name()
    for produce in all_produce.copy():
        if current_season in produce["season"]:
            produce["in_season"] = True
            in_season.append(produce)
        else:
            produce["in_season"] = False
            out_of_season.append(produce)
    return render_template("produce.html", list_of_produce=in_season + out_of_season)


if __name__ == "__main__":
    app.run(debug=True)
