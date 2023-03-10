from flask import Blueprint
from .contact_blueprint import contact_blueprint
from .property.select_property_blueprint import select_property_blueprint
from .feature.feature_list_bluebrint import feature_list_blueprint
from .feature.select_feature_blueprint import select_feature_blueprint
from .property.property_list_blueprint import property_list_blueprint
from.login.login_blueprint  import login_blueprint
from .login.singup_buleprint import singup_blueprint


api_blueprint=Blueprint('api_blueprint',__name__)

api_blueprint.register_blueprint(
    contact_blueprint,url_prefix='/contact'
)
api_blueprint.register_blueprint(
 select_property_blueprint,url_prefix='/select_property'
)
api_blueprint.register_blueprint(
    feature_list_blueprint,url_prefix='/feature_list'
)
api_blueprint.register_blueprint(
    select_feature_blueprint,url_prefix='/select_feature'
)

api_blueprint.register_blueprint(
    property_list_blueprint,url_prefix='/property_list'
)
api_blueprint.register_blueprint(
    login_blueprint,url_prefix='/login'
)
api_blueprint.register_blueprint(
    singup_blueprint,url_prefix='/signup'
)