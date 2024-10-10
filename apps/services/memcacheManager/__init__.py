
from flask import Blueprint

blueprint = Blueprint(
    'memcache_manager_blueprint',
    __name__,
    url_prefix='/api'
)
