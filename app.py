from flask import Flask,  render_template, request, redirect, url_for, jsonify, flash
from flask_cors import CORS
from database.db import mongo_connect
import json
import pymongo
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/index")
@app.route('/')
def index():
    client = mongo_connect()
    site_list = json.loads(open("static/site.json", "r", encoding="utf-8").read())
    post_list = client.rss_mail_service.post.find()
    now = datetime.datetime.now()
    cnow = now.replace(hour=9, minute=0, second=0)
    new_post = client.rss_mail_service.post.find({"date":{"$lt":cnow}})
    client.close()
    return render_template("index.html",
            site_list=site_list["site"],
            post_list=list(post_list),
            new_post=list(new_post),
            today = now, up_day = cnow.strftime('%Y-%m-%d %H:%M:%S'))


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
