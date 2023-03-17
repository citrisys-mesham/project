from flask import Blueprint,request,render_template,jsonify

import json,os
from dto.request.forgot import UpdateForgotRequest
from repositories.forgot_password import ForgotRepository
from usecase.forgot_password import ForgotPasswordUsecase

forgot_password_blueprint=Blueprint('forgot_password_blueprint',__name__)
@forgot_password_blueprint.route('/forgot_password',methods=['POST'])
def forgot_password():
    username =request.form["username"]
    password =request.form["password"]

    req = UpdateForgotRequest(username,password)
    print("req",req)
  
    repo = ForgotRepository()
    print("repo",repo)
    update_egg = ForgotPasswordUsecase(repo)
    print("update_egg",update_egg)
    res = update_egg.handle(req)
    print("res",type(res))
    if len(res)==0:
        return render_template("forgot.html")
    else:
        return render_template("login.html")