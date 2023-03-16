from flask import Blueprint,request,render_template
from dto.request.login.singup import SingupRequest
from repositories.login.singup import SingupRepo
from usecase.login.singup import SingupUsecase

singup_blueprint=Blueprint('singup_blueprint',__name__)

@singup_blueprint.route("/",methods=["POST"])
def singup_get():
    username =request.form["username"]
    password =request.form["password"]
    req=SingupRequest(username,password)
    repo=SingupRepo()
    get_login=SingupUsecase(repo)
    out=get_login.handle(req)
    return render_template("login.html")