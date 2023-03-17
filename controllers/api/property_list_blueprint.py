<<<<<<< HEAD
from flask import Flask,request,Blueprint,render_template
=======
from flask import Flask,request,Blueprint,render_template,redirect,url_for
>>>>>>> a5a9baba330bd160ce76a9bd7b6c7e014274535f
from repositories.property_list import PropertyListRepo
from usecase.property_list import PropertyListCase

property_list_blueprint=Blueprint('property_list_blueprint',__name__)

@property_list_blueprint.route('/all')

<<<<<<< HEAD
def get_data():
=======
def all():
>>>>>>> a5a9baba330bd160ce76a9bd7b6c7e014274535f
    repo=PropertyListRepo()
    case=PropertyListCase(repo)
    out=case.get()

<<<<<<< HEAD
    return render_template('property_list.html',property=out)
=======
    # return redirect(url_for('api_blueprint.feature_list_blueprint.all'))
    return render_template("property_list.html",property=out)
>>>>>>> a5a9baba330bd160ce76a9bd7b6c7e014274535f
