from flask import Flask, flash, redirect, render_template, request, session

# initialize Flask app
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return "hello, world"

