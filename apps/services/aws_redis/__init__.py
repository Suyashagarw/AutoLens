
from flask import Blueprint

blueprint = Blueprint(
    'cache_blueprint',
    __name__,
    url_prefix='/cache'
)
