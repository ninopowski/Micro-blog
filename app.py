import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry = request.form.get("content")
        formated_date = datetime.datetime.today().strftime("%d-%m-%Y")
        entries.append((entry, formated_date))

    entries_with_date = [
        (
        entry[0],
        entry[1],
        datetime.datetime.strptime(entry[1], "%d-%m-%Y").strftime("%b %d")
        )
        for entry in entries
    ]
    return render_template("home.html", entries=entries_with_date)



if __name__ == "__main__":
    app.run(debug=True)