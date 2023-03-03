from flask import Blueprint
from .contact_blueprint import contact_blueprint
from .property_blueprint import property_blueprint
api_blueprint=Blueprint('api_blueprint',__name__)

api_blueprint.register_blueprint(
    contact_blueprint,url_prefix='/contact'
)
api_blueprint.register_blueprint(
 property_blueprint,url_prefix='/property'
)