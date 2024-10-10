
from flask import Blueprint

blueprint = Blueprint(
    'cloudWatch_blueprint',
    __name__,
    url_prefix='/cloudWatch'
)
