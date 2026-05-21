from flask import Flask, render_template
import json
from datetime import datetime


def process_offer_data(data_to_process):
    offer_data = []
    for offer in data_to_process:
        for vendor in all_vendors:
            if vendor["id"] == offer["vendor_id"]:
                offer["vendor_name"] = vendor["name"]
                offer["vendor_address"] = vendor["address"]
                offer["vendor_image"] = vendor["image"]
        for produce in all_produce:
            if produce["id"] == offer["produce_id"]:
                offer["produce_name"] = produce["name"]
                offer["produce_image"] = produce["image"]
        offer_data.append(offer)
    return offer_data


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


with open("data/produce.json", "r", encoding="utf8") as f:
    all_produce = json.load(f)

with open("data/vendors.json", "r", encoding="utf8") as f:
    all_vendors = json.load(f)

with open("data/offers.json", "r", encoding="utf8") as f:
    all_loaded_offers = json.load(f)
    all_offers = process_offer_data(all_loaded_offers)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vendors")
def vendors():
    updated_vendors = []

    for original_vendor in all_vendors.copy():
        vendor = original_vendor.copy()
        vendor["produce_names"] = []

        for offer in all_offers:
            if offer["vendor_id"] == vendor["id"]:
                vendor["produce_names"].append(offer["produce_name"])

        updated_vendors.append(vendor)

    return render_template("vendors.html", list_of_vendors=updated_vendors)


@app.route("/produce")
def produce():
    in_season = []
    out_of_season = []
    current_season = get_season_name()
    for original_produce in all_produce.copy():
        produce = original_produce.copy()
        if current_season in produce["season"]:
            produce["in_season"] = True
            in_season.append(produce)
        else:
            produce["in_season"] = False
            out_of_season.append(produce)
    return render_template("produce.html", list_of_produce=in_season + out_of_season)


@app.route("/produce/<produce_id>")
def individual_produce(produce_id):
    offers_for_produce = []

    for i in all_produce:
        if i["id"] == int(produce_id):
            produce = i

    for original_offer in all_offers.copy():
        offer = original_offer.copy()
        if offer["produce_id"] == int(produce_id):
            offers_for_produce.append(offer)

    return render_template(
        "individual_produce.html",
        offers_for_produce=offers_for_produce,
        produce=produce,
    )


@app.route("/apply")
def apply():
    return render_template("submission_form.html")


@app.route("/apply/submit", methods=["POST"])
def submit():
    return render_template("receipt.html")


if __name__ == "__main__":
    app.run(debug=True)
