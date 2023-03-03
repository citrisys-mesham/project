from flask import Blueprint
from .contact_blueprint import contact_blueprint

api_blueprint=Blueprint('api_blueprint',__name__)

api_blueprint.register_blueprint(
    contact_blueprint,url_prefix='/contact'
)