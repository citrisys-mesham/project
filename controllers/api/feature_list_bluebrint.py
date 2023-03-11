from flask import Flask,request,Blueprint,render_template
from repositories.feature_list import FeatureListRepo
from usecase.feature_list import FeatureListCase
feature_list_blueprint=Blueprint('feature_list_blueprint',__name__)

@feature_list_blueprint.route('/all')

def all():
    repo=FeatureListRepo()
    case=FeatureListCase(repo)
    out=case.get()
    
    return render_template('feature_list.html',features=out)
    

    
