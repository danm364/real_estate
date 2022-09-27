from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash



# initialize Flask app
app = Flask(__name__)
#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#secret key
app.config['SECRET_KEY'] = 'dev'

app.config["TEMPLATES_AUTO_RELOAD"] = True
#initalize database
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True )
    hash = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/register")
def register():

    if request.method == "POST":
        password = request.form.get("password")
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        users = Users(
            name = request.form['username']
            hash = hashed_password

        )
        

    return render_template("register.html")