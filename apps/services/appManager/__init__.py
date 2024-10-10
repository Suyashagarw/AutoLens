from flask import Blueprint

blueprint = Blueprint(
    'appManager_blueprint',
    __name__,
    url_prefix='/appManager'
)
