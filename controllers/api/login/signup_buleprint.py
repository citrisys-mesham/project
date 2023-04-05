from flask import Blueprint,request,render_template
from dto.request.login.singup import SingupRequest
from repositories.login.singup import SingupRepo
from usecase.login.singup import SingupUsecase

signup_blueprint=Blueprint('signup_blueprint',__name__)

@signup_blueprint.route("/signup",methods=["POST"])
def signup_get():
    username =request.form["username"]
    password =request.form["password"]
    req=SingupRequest(username,password)
    repo=SingupRepo()
    get_login=SingupUsecase(repo)
    out=get_login.handle(req)
    if out:
      return render_template("welcome.html",username=username)
    else:
        return render_template("login.html", error="Signup failed. Please try again.")    