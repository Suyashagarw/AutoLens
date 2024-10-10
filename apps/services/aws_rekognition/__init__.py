
from flask import Blueprint

blueprint = Blueprint(
    'rekognition_blueprint',
    __name__,
    url_prefix='/image'
)
