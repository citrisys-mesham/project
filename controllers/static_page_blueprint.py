from flask import Blueprint, render_template

static_blueprint = Blueprint('static_blueprint', __name__)

@static_blueprint.route('/')
def index():
    return render_template("login.html")


@static_blueprint.route('/forgot')
def forgot():
    return render_template("forgot.html")
