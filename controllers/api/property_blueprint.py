from flask import Blueprint,request,jsonify
import json
from dto.request.property import AddPropertyRequest
from repositories.property import PropertyRepo
from usecase.property import PropertyCase
property_blueprint=Blueprint('property_blueprint',__name__)

@property_blueprint.route('/',methods=['POST'])
def get_data():
    data=json.loads(request.get_data())
    req=AddPropertyRequest(**data)
    repo=PropertyRepo()
    case=PropertyCase(repo)
    output=case.use_case(req)

    return jsonify(output)