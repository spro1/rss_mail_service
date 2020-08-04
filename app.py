from flask import Flask,  render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Email(db.Model):
    """create email list table"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)

    def __init__(self, email):
        self.email = email


@app.route("/index")
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/insert_email", methods=["POST"])
def insert_email():
    if request.method == "POST":
        email = request.form["email"]
        new_email = Email(email=email)
        db.session.add(new_email)
        db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    app.secret_key = "123"
    app.run(debug=True)
