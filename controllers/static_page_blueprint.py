from flask import Blueprint, render_template

static_blueprint = Blueprint('static_blueprint', __name__)

@static_blueprint.route('/')
def index():
    return render_template("/home.html")

@static_blueprint.route('/login')
def login():
    return render_template("login.html")

@static_blueprint.route("/singup")
def signup():
    return render_template("singup.html")

@static_blueprint.route("/forgot")
def forgot():
    return render_template("forgot_password.html")


# @static_blueprint.route('/login')
# def room():
#     return render_template("login/login.html")