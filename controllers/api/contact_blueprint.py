from flask import Blueprint,request,jsonify
import json
from dto.request.contact import AddContactRequest
from repositories.contact import ContactRepo
from usecase.contact import ContactUseCase

contact_blueprint=Blueprint('contact_blueprint',__name__)

@contact_blueprint.route('/',methods=["POST"])

def insert_contact():
    
    data=json.loads(request.get_data())
    print(data,type(data))

    contact_req=AddContactRequest(**data)
    repo=ContactRepo()
    use=ContactUseCase(repo)
    output=use.handle(contact_req)        
    return jsonify(output)


     