from flask import Flask,request,Blueprint,render_template
from repositories.property_list import PropertyListRepo
from usecase.property_list import PropertyListCase

property_list_blueprint=Blueprint('property_list_blueprint',__name__)

@property_list_blueprint.route('/all')

def get_data():
    repo=PropertyListRepo()
    case=PropertyListCase(repo)
    out=case.get()

    return render_template('property_list.html',property=out)