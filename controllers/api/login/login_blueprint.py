from flask import Blueprint, request, session, redirect, url_for, render_template
from repositories.login.login import LoginRepo
from usecase.login.Login import LoginUsecase
from dto.request.login.login import LoginRequest


login_blueprint=Blueprint('login_blueprint',__name__)

@login_blueprint.route("/login",methods=["POST"])
def login_get():
   
    input=request.form["username"]
    input1=request.form["password"]
    # input1=input.to_dict(flat=False)
    print("logininput",input1,input)
    req=LoginRequest(input,input1)
    print("loginreq",req)
    repo=LoginRepo()
    print("loginrepo",repo)
    get_login=LoginUsecase(repo)
    print("loginget",get_login)
    case=get_login.handle(req)
    print("logincase",case,type(case))

    if len(case)==0:
        print("checking")
        return render_template('login.html')
        
    else:
       return render_template('contact.html')
        
        # return redirect(url_for('api_blueprint.feature_list_blueprint.all'))

