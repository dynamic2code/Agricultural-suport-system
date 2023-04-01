from flask import Blueprint, render_template
import test

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route("/")
def login():
    return render_template("login.html")

@app_blueprint.route("/content")
def content():
    return render_template("content.html",test.farming_activity(report), )
