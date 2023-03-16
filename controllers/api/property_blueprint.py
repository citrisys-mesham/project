from flask import Blueprint,request,jsonify
import json

property_blueprint=Blueprint('property_blueprint',__name__)

@property_blueprint.route('/',methods=['POST'])
def get_data():
    new= request.form
    new1=new.to_dict(flat=False)
    print (type(new1),new1)
   
    return new1