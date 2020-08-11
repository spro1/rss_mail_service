from flask import Flask,  render_template, request, redirect, url_for, jsonify, flash
from flask_cors import CORS
from database.db import mongo_connect
import json
import pymongo

app = Flask(__name__)
CORS(app)

@app.route("/index")
@app.route('/')
def index():
    client = mongo_connect()
    site_list = json.loads(open("static/site.json", "r", encoding="utf-8").read())
    post_list = client.rss_mail_service.post.find()
    client.close()
    return render_template("index.html", site_list=site_list["site"], post_list=post_list)


@app.route("/insert_email", methods=["POST"])
def insert_email():
    if request.method == "POST":
        client = mongo_connect()
        collection = client.rss_mail_service.email
        email = request.form["email"]
        if email is "": flash("This email is wrong")
        elif collection.find_one({"email": email}) is None:
            collection.insert({"email": email, "on": 1})
            flash("Email registration was successful.")
        else:
            flash("This email has already been registered.")
        client.close()
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = "123"
    app.run("0.0.0.0", debug=True, ssl_context=('./cert/server.crt','./cert/server.key'))
