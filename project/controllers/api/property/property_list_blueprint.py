from flask import Flask,request,Blueprint,render_template,redirect,url_for
from repositories.property.property_list import PropertyListRepo
from usecase.property.property_list import PropertyListCase

property_list_blueprint=Blueprint('property_list_blueprint',__name__)

@property_list_blueprint.route('/all')

def all():
    repo=PropertyListRepo()
    case=PropertyListCase(repo)
    out=case.get()

    # return redirect(url_for('api_blueprint.feature_list_blueprint.all'))
    return render_template("property_list.html",property=out)