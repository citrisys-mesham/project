from flask import Blueprint,request,jsonify,render_template,redirect,url_for
import json
from dto.request.contact import AddContactRequest
from repositories.contact import ContactRepo
from usecase.contact import ContactUseCase

contact_blueprint=Blueprint('contact_blueprint',__name__)
property_list_blueprint=Blueprint('property_list_blueprint',__name__)
@contact_blueprint.route('/',methods=["POST"])

def insert_contact():
    
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login_blueprint.login_get'))

    Door_no =request.form["door"]
    Street =request.form["street_name"]
    city =request.form["city"]
    State =request.form["state"]
    Country =request.form["country"]
    zip =request.form["zip"]
    phone=request.form["phone"]
    email =request.form["email"]
   
    # data=json.loads(data1)
    print(Door_no,type(Door_no),State)

    contact_req=AddContactRequest(Door_no,Street,city,State,Country,zip,phone,email)
    print("conacat_req",contact_req)
    repo=ContactRepo()
    print("repo",repo)
    use=ContactUseCase(repo)
    print("con_use",use)
    output=use.handle(contact_req) 
    print("output",output)
    return redirect(url_for('api_blueprint.property_list_blueprint.all'))
        

     