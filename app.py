from flask import Flask,  render_template, request, redirect, url_for
from flask_cors import CORS
from database.db import mongo_connect
import json

app = Flask(__name__)
CORS(app)

@app.route("/index")
@app.route('/')
def index():
    site_list = json.loads(open("static/site.json", "r", encoding="utf-8").read())
    return render_template("index.html", site_list=site_list["site"])


@app.route("/insert_email", methods=["POST"])
def insert_email():
    if request.method == "POST":
        client = mongo_connect()
        collection = client.rss_mail_service.email
        email = request.form["email"]
        if collection.find_one({"email": email}) is None:
            collection.insert({"email": email, "on": 1})
        else:
            print("already")
        client.close()
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = "123"
    app.run(debug=True)
