
from flask import Blueprint

blueprint = Blueprint(
    'photoUpload_blueprint',
    __name__,
    url_prefix='/photoUpload'
)
