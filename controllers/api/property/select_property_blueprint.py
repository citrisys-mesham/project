from flask import Blueprint,request,jsonify,render_template,redirect,url_for
import json
from dto.request.select_property import AddPropertyRequest
from repositories.property.select_property import PropertyRepo
from usecase.property.select_property import PropertyCase

select_property_blueprint=Blueprint('select_property_blueprint',__name__)

@select_property_blueprint.route('/show',methods=['POST'])
def insert_property():
    input=request.form.getlist('property[]')
    print("input",input)
    req=AddPropertyRequest(input)
    repo=PropertyRepo()
    case=PropertyCase(repo)
    out=case.use_case(req)
    print("out",type(out),out)
    property_list = "\n".join([f"{i+1}. {feature[0]}" for i, feature in enumerate(out)])
    property_list = property_list.rstrip() 
    print("property_list",property_list)

    # return render_template('image.html')
    # return "sucessfully insert THANK YOU"
    return redirect(url_for('api_blueprint.feature_list_blueprint.all'))
    # return render_template('selected_property.html',formatted_property=property_list)
# def get_data():
#     data=json.loads(request.get_data())
#     req=AddPropertyRequest(**data)
#     repo=PropertyRepo()
#     case=PropertyCase(repo)
#     output=case.use_case(req)

#     return jsonify(output)

