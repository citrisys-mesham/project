from flask import Blueprint,request,render_template
from dto.request.login.signup import SignupRequest
from repositories.login.signup import SignupRepo
from usecase.login.signup import SignupUsecase

signup_blueprint=Blueprint('signup_blueprint',__name__)

@signup_blueprint.route("/",methods=["POST"])
def signup_get():
    username =request.form["username"]
    password =request.form["password"]
    req=SignupRequest(username,password)
    repo=SignupRepo()
    get_login=SignupUsecase(repo)
    out=get_login.handle(req)
    return render_template("login.html")