from flask import Blueprint,request,render_template
from dto.request.select_feature import FeatureReq
from repositories.feature.select_feature import SelectFeatureRepo
from usecase.feature.select_feature import SelectFeatureUse
select_feature_blueprint=Blueprint('select_feature_blueprint',__name__)

@select_feature_blueprint.route('/add',methods=['POST'])
def insert_feature():
    input=request.form.getlist('features[]')
    print('input:',input)
    print('ok2')
    req=FeatureReq(input)
    repo=SelectFeatureRepo()
    case=SelectFeatureUse(repo)
    out=case.data_case(req)
    features=out
    print(type(features))
    
    features_list = "\n".join([f"{i+1}. {feature[0]}" for i, feature in enumerate(features)])
    features_list = features_list.rstrip() 
    print(features_list)
    # return render_template('selected_feature.html', formatted_features=features_list)
    # return "sucessfully insert THANK YOU"
    return render_template('image.html')
