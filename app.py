from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import os, requests

app = Flask(__name__)

app.config["SESSION_PERMENANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    # call = requests.get("https://api.unsplash.com/photos/0X6HTVHn_kg/statistics?client_id=hp-n5d8W2_nK0fG91scJv4G9dGCGlxF_7VKonhj0TX8")
    # data = call.json()
    return render_template("index.html", name=session.get("name"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")