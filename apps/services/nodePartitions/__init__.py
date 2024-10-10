
from flask import Blueprint

blueprint = Blueprint(
    'managerApp_blueprint',
    __name__,
    url_prefix='/managerApp'
)
