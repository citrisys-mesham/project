from flask import Blueprint,request,jsonify
import json
from dto.request.property import AddPropertyRequest
from repositories.property import PropertyRepo
from usecase.property import PropertyCase
property_blueprint=Blueprint('property_blueprint',__name__)

@property_blueprint.route('/',methods=['POST'])
def get_data():
    new= request.form
    new1=new.to_dict(flat=False)
    print (type(new1),new1)
    # data=json.loads(request.get_data())
    # print (data)
    # req=AddPropertyRequest(**data)
    # repo=PropertyRepo()
    # case=PropertyCase(repo)
    # output=case.use_case(req)

    # return jsonify(output)=
    return new