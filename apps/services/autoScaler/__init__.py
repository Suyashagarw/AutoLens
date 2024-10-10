from flask import Blueprint

blueprint = Blueprint(
    'autoScaler_blueprint',
    __name__,
    url_prefix='/autoScaler'
)
