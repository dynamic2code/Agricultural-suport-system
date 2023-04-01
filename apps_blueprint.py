from flask import Blueprint, render_template

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route("/")
def login():
    return render_template("./templates/login.html")

