from flask import Blueprint
from .contact_blueprint import contact_blueprint
from .property_blueprint import property_blueprint
from .feature_list_bluebrint import feature_list_blueprint
from .select_feature_blueprint import select_feature_blueprint
api_blueprint=Blueprint('api_blueprint',__name__)

api_blueprint.register_blueprint(
    contact_blueprint,url_prefix='/contact'
)
api_blueprint.register_blueprint(
 property_blueprint,url_prefix='/property'
)
api_blueprint.register_blueprint(
    feature_list_blueprint,url_prefix='/feature_list'
)
api_blueprint.register_blueprint(
    select_feature_blueprint,url_prefix='/select_feature'
)