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

    return render_template("home.html", entries=entries)



if __name__ == "__main__":
    app.run(debug=True)