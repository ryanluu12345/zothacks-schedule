from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def main():
    with open("one_day_schedule.json") as schedule:
        events = json.load(schedule)
    return render_template("index.html", events = events)


if __name__ =="__main__":
    app.run()