
from flask import Blueprint

blueprint = Blueprint(
    'sqs_blueprint',
    __name__,
    url_prefix='/queue'
)
