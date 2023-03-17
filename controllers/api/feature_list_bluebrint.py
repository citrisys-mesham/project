from flask import Flask,request,Blueprint,render_template
from repositories.feature_list import FeatureListRepo
from usecase.feature_list import FeatureListCase
feature_list_blueprint=Blueprint('feature_list_blueprint',__name__)

@feature_list_blueprint.route('/all')

<<<<<<< HEAD
def get_data():
=======
def all():
>>>>>>> a5a9baba330bd160ce76a9bd7b6c7e014274535f
    repo=FeatureListRepo()
    case=FeatureListCase(repo)
    out=case.get()
    
    return render_template('feature_list.html',features=out)
    

    
