import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://programkogjj:programovanijebest!?@cluster0.sryitvq.mongodb.net/")

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))

    entries_formatted = [
        (
           entry[0],
           entry[1],
           datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]

    return render_template("add.html", entries=entries_formatted)